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

# Видимость переменных

x = "global"
def foo():
    print("x inside :", x)
foo()
print("x outside:", x)

x = "global"
def foo():
    global x
    y = "local"
    x = x*2 + y*2
    print(x)
foo()

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()


# Lambda функции

asd = (lambda x: x + 1)
print(asd(2))

colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
print(sorted(colors, key=lambda s: s.casefold()))
# Результат: ['cyan', 'Goldenrod', 'purple', 'Salmon', 'turquoise']


# Рекурсия
import sys
sys.setrecursionlimit(10**6)

def getTotal(n, total):
    print(n)
    if n == 0: # базовое условие
        return total
    else:
        return getTotal(n-1, (total+(n)))

print(getTotal(5, 0))

# Декораторы

def example_function(param1 = "test"):
    return param1
print(example_function())
variable = example_function
print(variable())

def example_function():
    def under_function(param1):
        print(param1)
    print(under_function("test"))
example_function()

def example_function():
    def under_function(param1):
        print(param1)
    return under_function
variable = example_function()
print(variable("test"))


def self_decorator(function_to_decorate):
    def wrap_original_function(): # объявляем вложенную функцию
        print("before")
        function_to_decorate() # вызываем оригинальную функцию
        print("after")
    return wrap_original_function # возвращаем функцию в качестве результата работы
def easy_function(): # определяем простую функцию
    print("i am just printinng this")
decorated_function = self_decorator(easy_function) # декорируем функцию
decorated_function()


@self_decorator
def easy_function():
    print("i am just printing this")
easy_function()


def self_decorator(function_to_decorate):
    def wrap_original_function(before_arg, after_arg):
        print(before_arg)
        function_to_decorate(before_arg, after_arg)
        print(after_arg)
    return wrap_original_function

@self_decorator
def easy_function(before_arg, after_arg):
    print("my args", before_arg, after_arg)

easy_function("this is before", "this is after")

def self_decorator(function_to_decorate):
    def wrap_original_function(*args, **kwargs):
        function_to_decorate(*args, **kwargs)
    return wrap_original_function


def parametarized_decorator(decorator_arg1, decorator_arg2):
    print("my decorator args", decorator_arg1, decorator_arg2)
    def custom_decorator(func):
        def wrapped(function_arg1, function_arg2) :
            return func(function_arg1, function_arg2)
        return wrapped
    return custom_decorator

@parametarized_decorator("test1", "test2")
def easy_function(function_arg1, function_arg2):
    print(function_arg1, function_arg2)

easy_function("test4", "test5")
