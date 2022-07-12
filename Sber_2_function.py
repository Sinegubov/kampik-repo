def append(my_list):
    my_list.append(1)
x = [0]
append(x)
print(x)

def append1(my_list):
    my_list = [0, 1]
x1 = [0]
append1(x1)
print(x1)

def print_func(str_to_print):
    print(str_to_print)
print_func("test") # так отработает корректно

def print_func(str_to_print, int_to_print=50):
    print(str_to_print)
    print(int_to_print)
print_func(str_to_print="test")

def print_func(str_to_print, int_to_print):
    print(str_to_print)
    print(int_to_print)
print_func(int_to_print=50, str_to_print="test")


# *args и **kwargs

def summator(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)
summator(3, 5)
summator(4, 5, 6, 7)
summator(1, 2, 3, 5, 6)


def inside_kwargs(**kwargs):
    print("kwargs type is", type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
inside_kwargs(Company="Sberbank", info="python_course", location="online")