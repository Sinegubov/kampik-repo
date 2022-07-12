# Вопрос 1 Как можно использовать список в качестве стека или очереди?
list_fifo = []
for i in range(5):
    list_fifo.append(i)

print(list_fifo)
list_fifo.pop(0)
print(list_fifo)

list_filo = []
for i in range(5):
    list_filo.append(i)

print(list_filo)
list_fifo.pop()
print(list_fifo)

# Вопрос 2 Если внутрь кортежа положить список, возможно ли использовать данный кортеж в качестве ключа словаря?
simple_list = [1, 2, 3]
simple_tuple = (1, 2, 2)
print(simple_tuple)

simple_dict = {}
simple_dict[simple_tuple] = 1
print(simple_dict)

# Вопрос 3 Как с помощью множества удалить дублирование в списке?
simple_list = [1, 2, 3]
simple_list = simple_list * 2
print(simple_list)
simple_list = list(set(simple_list))
print(simple_list)

# Вопрос 4 Как использовать функцию get() словаря и чем она может быть полезна, если значения в словаре нет?
simple_dict = {1:1, 2:3, 3:[1,2,3]}
print(simple_dict)

print(simple_dict.get(5, []))

# Вопрос 5 Что такое срезы у списков и как с помощью них можно развернуть список в обратную сторону?
simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(simple_list[0:4:2])
print(simple_list[::-1])

# Вопрос 6 Как растет потребление памяти, если в структуру положить 1 - 10 - 100 - 1000 - 1 000 000 других объектов?
import sys

print(sys.getsizeof([1]))

def simple_get_true_size(obj, mem=None):
    size = sys.getsizeof(obj)
    if mem is None:
        mem = set()

    obj_id = id(obj)
    if obj_id in mem:
        return 0
    mem.add(obj_id)

    if isinstance(obj, dict):
        size += sum([simple_get_true_size(key, mem) for key in obj.keys()])
        size += sum([simple_get_true_size(value, mem) for value in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += simple_get_true_size(obj, __dict__, mem)
    elif hasattr(obj, '__iter__'):
        size += sum([simple_get_true_size(i, mem) for i in obj])
    return size

print(simple_get_true_size(1))
print(simple_get_true_size([]))
print(simple_get_true_size({100}))
# Вопрос 7 Есть ли разница в использовании памяти структурой данных на 32 / 64 разрядной машине?


# Вопрос 8 Очищается ли память, если применить del() к структуре данных?

a = [1,2,3,4,5]
a.append([6, 7])
print(a)

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1 :: 3]
print(b)


print("asdasdasdasdasdasdasdasdasdasdsad")

Dict1 = {"test": 1}
print(Dict1)
#Dict2 = {dict(test=1): 'ints can be keys'}
#print(Dict2)
#Dict4 = {[1, 2]: 'strings can be keys'}
#print(Dict4)
Dict5 = {(1, 2): 'lists can NOT be keys'}
print(Dict5)
Dict6 = {(3+2j): 'lists can NOT be keys'}
print(Dict6)
Dict7 = {len: 'lists can NOT be keys'}
print(Dict7)
#Dict8 = {(1, [], 2): 'lists can NOT be keys'}
#print(Dict8)