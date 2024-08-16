numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100, 14, 15, 1000] # цифры можно заменить на любые в любом порядке
numbers = [n for n in numbers if type(n) == int and n != 0 and n !=1] # проверяем список
primes = [] # создаем список простых чисел
not_primes = [] # создаем список составных чисел
for i in range(2, int(max(numbers))+1): # создаем цикл делимых до максимального числа в списке
    for j in range(2, int(max(numbers))): # создаем цикл делителей
        a = (i % j) # выводим остаток от деления
        if int(a) == 0 and {i} != {j}: # проверяем соответствие условиям
            not_primes.append(i) # добавляем составное число в список
        else:
            primes.append(i) # добавляем оставшиеся числа в список
primes = [m for m in primes if m in numbers] # оставляем только числа из первоначального списка
not_primes = [p for p in not_primes if p in numbers] # оставляем составные числа из первоначального списка
res = [k for k in primes if k not in not_primes] # удаляем совпадающие числа
print('Простые числа:', sorted(list(set(res)))) # оставляем уникальные значения и упорядочиваем их
print('Составные числа:', sorted(list(set(not_primes)))) #оставляем уникальные значения и упорядочиваем их