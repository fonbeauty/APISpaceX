import string


def task1():
    s1 = 'Hello'
    s2 = 'World'
    s3 = '!'

    result1 = s1 + ' ' + s2 + ' ' + s3
    result2 = f'{s1} {s2} {s3}'
    result3 = '{k1} {k2} {k3}'.format(k3=s1, k1=s2, k2=s3)

    print(result1)
    print(result2)
    print(f'Format result {result3}')


def task2(name, have_a_nice):
    print(f'Hello {name}, have a nice {have_a_nice}')


def task3(string1, sub):
    if sub in string1:
        print('Yes')
    else:
        print('No')


def task4(string1: str, sub: str):
    print('Количество вхождений подстроки ' + str(string1.count(sub)))
    pass


def task5(string1: str, sub: str):
    print(string1.find('df'))
    print(string1.rfind('d'))
    pass


def task6(name: str) -> str:
    str1 = name.replace('_', ' ')
    str2 = str1.capitalize()
    str3 = str2.split(' ')
    str4 = '****'.join('asdfasdfasdfasdf')
    return str2


def task7(string1: str) -> str:
    result = string1[1::2]
    return result


def task8(string1: str) -> str:
    result = string1[:5:-1]
    return result


punctuation_char = ',.:;'


def task9(palindrom: str) -> bool:
    without_punctuation = ''
    palindrom = palindrom.lower()
    palindrom = palindrom.replace(' ', '')
    for char in palindrom:
        if char not in string.punctuation:
            without_punctuation += char

    reverse_palindrome = without_punctuation[::-1]
    return without_punctuation == reverse_palindrome


def task10(stroka: str) -> str:
    str1 = stroka.split(' ')
    str1.sort()
    str2 = ' '.join(str1)

    return str2


def task11(stroka: str, anagramma_candidate: str) -> str:
    stroka = stroka.lower().replace(' ', '')
    anagramma_candidate = anagramma_candidate.lower().replace(' ', '')
    if len(stroka) == len(anagramma_candidate):
        stroka_sorted = sorted(stroka)
        anagramma_candidate_sorted = sorted(anagramma_candidate)
        if stroka_sorted == anagramma_candidate_sorted:
            return f'{stroka} и {anagramma_candidate} являются анаграммами'
        else:
            return f'{stroka} и {anagramma_candidate} НЕ являются анаграммами'
    else:
        return f'{stroka} и {anagramma_candidate} имеют разное количество символов, не анаграммы'


# return ''


# print(task9('рвал дед лавр'))
# print(task9('Коту тащат уток'))
# print(task9('Леша на полке клопа нашел'))
# print(task9('А роза упала на лапу Азора'))
# print(task9('Ишаку казак сено нес, казаку каши'))

# print(task10('Ишаку казак сено нес, казаку каши'))
# print(task10('Дана строка, необходимо сформировать строки из слов данной строки в алфавитном порядке'))

print(task11('Дана строка, необходимо', 'необходимо    строка,  Дана'))
print(task11('австралопитек', 'ватерполистка'))
print(task11('анкилозавр', 'разлиноыка'))

# print(task8(string='asdfasdfasdfasdf'))
# result = task7(string='asdfasdfasdfasdf')

# test_name = task6('test_create_user_200')

# task5(string='asdfasdfasdfasdf', sub='dfa')

# task2('Nikita', 'monday')
# task2('Bob', 'day')
# task2('Rosa', 'morning')

# task3(string='asdfasdfasdfasdf', sub='dfa')
# task4(string='asdfasdfasdfasdf', sub='dfa')
pass
