https://www.w3schools.com/python/python_sets_methods.asp

set (множество) - структура данных в Python. Она представляет собой неупорядоченную коллекцию уникальных элементов. В
некоторой степени, соответствует математическому множеству. Многие широко используемые математические операции,
применимые к множествам, существуют и в Python.

Есть два способа создания объекта set: set(iterable) и указание элементов в фигурных скобках { ... }.
Если попытаться создать множество так {} — то будет создан словарь, а не пустое множество.

# set1 = set()

set1 = {'111', '2222'}
set1.add('element1')
print(set1)
set1.clear()
print(set1)

set1 = {1, 2, 3, '4'}
set2 = {3, 2, 1, '5'}
print(f'equal {set1 == set2}')

print(f'Difference {set1 - set2}')
print(f'Difference {set1.difference(set2)}')

set1.discard('5')
print(f'Discard {set1}')

# set1.remove('5')

# print(f'Discard {set1}')

set1 = {1, 2, 3, '4', 5, 6}
set2 = {3, 2, 1, 5, 6, 7}
print(f'intersection {set1.intersection(set2)}')
print(f'intersection {set1 & set2}')

set1 = {1, 2, 3, '4'}
set2 = {3, 2, 1}

print(f'Returns whether two sets have a intersection or not {set1.isdisjoint(set2)}')

print(f'issubset {set1.issubset(set2)}')
print(f'issubset {set1 <= set2}')

print(f'issuperset {set1.issuperset(set2)}')
print(f'issuperset {set1 >= set2}')

print(f'pop {set1.pop()}')

set1 = {1, 2, 3, '4'}
set2 = {3, 2, 1, '5'}
print(f'symmetric_difference {set1.symmetric_difference(set2)}')
print(f'symmetric_difference {set1 ^ set2}')

print(f'union {set1.union(set2), set1}')
print(f'union {set1 | set2}')

set1 = {1, 2, 3, '4'}
set2 = {3, 2, 1, '5'}
set1.update(set2)
print(f'update {set1}')
set1 = {1, 2, 3, '4'}
set2 = {3, 2, 1, '5'}
set1 |= set2
print(f'update {set1}')
pass

Задачи:

1. Дано множество
numbers = {12, 434, 5467, -23, 5, 567, 3456, 234, 58, 578}
вывести сумму квадратов элементов

2. Дана стркоа текста, написать программу, которая определяет количество различных символов в строке.

3. Даны два множества:
st1 = {'x', '1', 'y', '2', 'z'}
st2 = {1, 2, 3, 4, 5, 6}
Узнайте в каком из них большее количество элементов.

4. Даны два числа:
num1 = 12345
num2 = 12321
Проверьте, что все цифры второго числа есть в первом числе.
print('yes') if else print('no')

5. Даны три переменные:
tst1 = 34
tst2 = [1, 2, 5]
tst3 = (6, 7, 8)
Создайте из всех их элементов множество.

6. Даны множество и две переменные:
st = {'18', '24', '34', '47', '81', '63'}
tst1 = '34'
tst2 = ('81', '12', '46')
Проверьте входят ли элементы каждой из переменной в множество.

7. Даны два числа:
num1 = 12345
num2 = 45123
Проверьте, что оба числа состоят из одинаковых цифр.

8. Напишите программу для определения общего количества различных слов в строке текста.
