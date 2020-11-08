#import tkinter
#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def compute_lambda(t):
    b = 33
    l_0 = 884
    t_0 = 100
    y = b * l_0 /(t-t_0)
    return y
f = open("lambda_exp.txt", "r")

t0_list =[]
t_list =[]

lambda_exp_list0 = []
lambda_exp_list = []


for line in f:

    t_lambda_list = line.split()

    t0_list.append(float(t_lambda_list [0]))

    lambda_exp_list0.append(float(t_lambda_list [1]))

f.close()

t_list = t0_list[1:13]
lambda_exp_list = lambda_exp_list0[1:13]

lambda_list =[compute_lambda(t) for t in t_list]

error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i] )
              for i in range(len(t_list))]

print("-" * 40)

print("|%7s | %7s | %7s |%8s |" % ("t","l(t)","exp(t)", "error"))

print( "-" * 40)

for i in range(len(t_list)):

    print("|%7d | %7.3f | %7.1f |%7.2f%% |"
          % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))

print("-" * 40)

max_error = max(error_list)

index_max_error = error_list.index(max_error)
print("Максимальная погрешность = %5.2f%%  при t = %5d"
      % (max_error * 100, t_list[index_max_error]))


min_error = min(error_list)

index_min_error = error_list.index(min_error)

print("Минимальная погрешность = %5.2f%%  при t = %5d"
      % (min_error * 100, t_list[index_min_error]))

avg_error = sum(error_list) / len(t_list)

print("Средняя погрешность = %5.2f%%" % (avg_error * 100))

line_th = plt.plot(t_list, lambda_list, label = 'теоретические')

line_exp = plt.plot(t_list, lambda_exp_list, label = 'экспериментальные')

# задаем стили для линий

plt.setp(line_exp, color= "blue", linestyle = "--", linewidth = 2 )

plt.setp(line_th, color= "red", linewidth = 2)

plt.legend()

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

plt.title("Значения теплопроводности")

plt.show()



