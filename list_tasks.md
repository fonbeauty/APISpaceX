1. Вспомним методы списков
   ['any', 1, [1, 2, 3], [1, 'symbols', 3, [3, 'in string']]]
2. Создайте список из трех имен. Добавьте в этот список два новых имени. Отсортируйте список. Удалить разными способами
   элемент списка.
   Распечайте полученный список.
2. Пусть дан список-матрица, который содержит три списка:
   matrix = [
   [11, 12, 13],
   [21, 22, 23],
   [31, 32, 33]
   ]
   Выведите всю матрицу в одном выражении.
   Выведите по отдельности каждую строку матрицы.
   Выведите по отдельности каждый элемент матрицы.
   Вывести с помощью цикла в красивом виде print(element, end=' ')
3. Дан список, надо удалить дубли - реализовать циклом и множествами, сравнить полученные списки
   [ 1, 3, 4, 5, 1, 2, 3, 5, 1, 6]
4. Реализовать создание списка от 1 до 10 циклом (range(1, 11)) и list comprehensions. Создать список квадратов count**2
   и кубов count**3 значений из спсика
   olo = [x for x in range(start, end + 1)]
5. Даны два списка, неободимо сложить эти списки, сложить значения элементов этих списков
   result_lt = [sum(i) for i in zip(lt1, lt2 )]
   lt1 = [6, 12, 18, 3, 6, 9]
   lt2 = [4, 8, 12, 2, 4, 6]
6. Даны два списка, необходимо найти пересечение этих списков, т.е. элементы, которые есть в обоих списках
7. Дан список фильмов, реализовать сортировку по элементам списка sorted(movies, key=lambda movie: movie[0]), по двум
   элементам списка
   movies = [
   [1994, 'The Shawshank Redemption', 9.2],
   [1999, 'Fight Club', 8.8],
   [1994, 'Pulp Fiction', 8.9],
   [1972, 'The Godfather', 9.2],
   [2008, 'The Dark Knight', 9.0],
   [1998, 'Godzilla', 6.8],
   [1989, 'Batman', 7.5]
   ]

https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/ref_func_zip.asp
https://www.w3schools.com/python/ref_func_sum.asp
https://www.w3schools.com/python/ref_func_sorted.asp