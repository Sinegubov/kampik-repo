#!/usr/local/bin/perl

$|++;

use Net::SNMP;
use Net::Telnet;

while(<STDIN>) {
	my $line = $_;

	if ( $line =~ /^(\d+\.\d+\.\d+\.\d+)\s(\d+\.\d+\.\d+\.\d+)\s*(\|.*)?$/ ) {
		my $host = $1;
		my $newhost = $2;
		my $newdef = $newhost; 
		$newdef =~ s/(\d+\.\d+\.\d+)\.\d+/$1.254/g;

		my ( $line, $type ) = get_info( $newhost, "xxx" );

		if ( $type ) {
			( $res, $session ) = connect_telnet( $newhost, "bicnet", "xxx" );
			if ( $res ne "OK" ) {
				( $res, $session ) = connect_telnet( $newhost, "bicnet", "xxx" )
			}
			$line .= " $res";
			if ( $res eq "OK" ) {
				$line .= " |";

				if ( $type eq "dlink"  ) {
					my @lines = $session->cmd( String => "show iproute " );
					my $def = "";
					foreach my $line ( @lines ) {
                                        	$def = $1 if ( $line =~ /0.0.0.0\/0\s+(\d+\.\d+\.\d+\.\d+)/ );
					}
					$line .= " DEF:$def";
					
					if ( $def ) {
						my @lines = $session->cmd( String => "delete iproute default $def",  );
					}
					else {
						$def = $host; $def =~ s/(\d+\.\d+\.\d+)\.\d+/$1/g;
						my @lines = $session->cmd( String => "delete iproute default $def.222" );
						my @lines = $session->cmd( String => "delete iproute default $def.1" );
					}
					my @lines = $session->cmd( String => "create iproute default $newdef" );
					$line .= " ROUTE-CHANGED:$newdef";

					open( FILE, "default_$type" );
					while( <FILE> ) {
						chomp;
						my @lines = $session->cmd( String => $_ );
					}
					close( FILE );
					$line .= " DEF-CONF-OK";

					my @lines = $session->cmd( String => "save", Timeout => 20 );
					$line .= " SAVE-OK";
				}
				elsif ( $type eq "huawei" ) {
					my @lines = $session->cmd( String => "n", Timeout => 3 );
					my @lines = $session->cmd( String => "su", Prompt => '/password:.*/i', Timeout => 3 );
					my @lines = $session->cmd( String => "VjhtGbdf", Timeout => 3 );
					my @lines = $session->cmd( String => "system-view", Timeout => 3 );

					my @lines = $session->cmd( String => "undo ip route-static 0.0.0.0 0.0.0.0" );
					my @lines = $session->cmd( String => "undo ip route-static 0.0.0.0 0.0.0.0" );
					my @lines = $session->cmd( String => "ip route-static 0.0.0.0 0.0.0.0 $newdef" );
					$line .= " ROUTE-CHANGED:$newdef";

					open( FILE, "default_$type" );
					while( <FILE> ) {
						chomp;
						my @lines = $session->cmd( String => $_ );
					}
					close( FILE );
					$line .= " DEF-CONF-OK";

					#my @lines = $session->cmd( String => "quit" );
					my @lines = $session->cmd( String => "save" );
					my @lines = $session->cmd( String => "y" );
					$line .= " SAVE-OK";
				}
				elsif ( $type eq "tplink-2600" || $type eq "tplink-2700" ) {
					$def = $host; $def =~ s/(\d+\.\d+\.\d+)\.\d+/$1/g;
					my @lines = $session->cmd( String => "enable", Prompt => '/password:.*/i', Timeout => 3 );
					my @lines = $session->cmd( String => "VjhtGbdf", Timeout => 3 );
					my @lines = $session->cmd( String => "configure", Timeout => 3 );
					my @lines = $session->cmd( String => "no ip route 0.0.0.0 0.0.0.0 $def.222" );
					my @lines = $session->cmd( String => "no ip route 0.0.0.0 0.0.0.0 $def.1" );
					my @lines = $session->cmd( String => "ip route 0.0.0.0 0.0.0.0 $newdef" );
					$line .= " ROUTE-CHANGED:$newdef";

					open( FILE, "default_$type" );
					while( <FILE> ) {
						chomp;
						my @lines = $session->cmd( String => $_ );
					}
					close( FILE );
					$line .= " DEF-CONF-OK";

					my @lines = $session->cmd( String => "exit" );
					my @lines = $session->cmd( String => "copy running-config startup-config" );
					$line .= " SAVE-OK";
				}
				elsif ( $type eq "eltex" ) {
				}
			}
		}


		print "$line\n";
        }
	else {
		print "$line\n";
	}

	
}


sub mac {
        my ( $line ) = @_;

        if( length($line) < 10 ){
                my $tmp;
                foreach $chr ( split //, $line ) {
                        $tmp .= sprintf ("%02X", ord($chr));
                }
                $line = $tmp;
        }

        $line =~ s/0x//;
        $line = join ":", ( $line =~ m/(..)/g );
        $line = uc $line;

        return $line;
}



sub get_info {
	my ( $host, $community ) = @_;

	my ( $ses, $err ) = Net::SNMP->session(
		'hostname'      => $host,
		'community'     => $community,
		'version'       => "2c",
		'timeout'       => 5,
		'retries'       => 2,
	);

	my $res = $ses->get_request(
		'varbindlist' => [
			"1.3.6.1.2.1.1.1.0",
			"1.3.6.1.2.1.2.2.1.6.1",
			"1.3.6.1.4.1.89.2.12.0",
			"1.3.6.1.4.1.2011.5.25.183.1.4.0",
			"1.3.6.1.2.1.17.1.1.0",
		],
	);

	my $info = $res->{'1.3.6.1.2.1.1.1.0'}; $info =~ s/[\r\n]//g;
	my $type;

	if ( $info =~ /(d-?link|des)/i ){
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.2.1.2.2.1.6.1'} ), $info );
		$type = "dlink";
	}
	elsif ( $info =~ /(dgs)/i ){
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.2.1.17.1.1.0'} ), $info );
		$type = "dlink-dgs";
	}
	elsif ( $info =~ /(snr-s\d+)/i ){
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.2.1.17.1.1.0'} ), $info );
		$type = "snr";
	}
	elsif ( $info =~ /(JetStream)/i ){
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.2.1.17.1.1.0'} ), $info );
		$type = "tplink-".( $info =~ /10G SFP\+ Slots/ ? "2700" : "2600" );
	}
	elsif ( $info =~ /(mes-?\d+)/i ) {
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.4.1.89.2.12.0'} ), $info );
		$type = "eltex";
	}
	elsif ( $info =~ /(huawei)/i ) {
		$line = sprintf ( "%s\t%s\t\|%s", $host, mac( $res->{'1.3.6.1.4.1.2011.5.25.183.1.4.0'} ), $info );
		$type = "huawei";
	}
	else {
		$line = sprintf ( "%s\t\t\|\%s", $host, $info );
	}

	return $line, $type;
}

sub connect_telnet {
        my ( $host, $login, $pass ) = @_;

        my $session = new Net::Telnet (
                Host => $host,
                Prompt => '/.+(\>|#|\]):?.*$/i',
                Timeout => 2,
                Errmode => 'return',
                cmd_remove_mode => 1,
        );
        return "ERR in connect", undef if ( !$session );


	my @lines = $session->waitfor( '/(login|user|username):.*/i' );
        return "ERR not loginned [1]", $session if ( $session->error() );
        @lines = $session->cmd( String => "$login", Prompt => '/password:.*/i', Timeout => 5 );
        return "ERR not loginned [2]", $session if ( $session->error() );
        @lines = $session->cmd( String => "$pass",  Timeout => 5 );
        return "ERR not loginned [3]", $session if ( $session->error() );

        return "OK", $session;
}

