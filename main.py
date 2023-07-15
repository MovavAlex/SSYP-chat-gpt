#
# k = int(input())
# a = ''
# c = 0
# while len(a) <= k:
#     c += 1
#     a += str(c)
#     if len(a) > k:
#         b = a[k-1]
#         break
#     elif len(a) == k:
#         b = str(a)[-1]
#         break
#
# print(int(b))


#
#
# k = int(input())
# strk = ''
# for i in range(k):
#     strk += str(i)
# if len(strk) >= k:
#     print(strk[k-1])


# k = int(input())
#
# strk = ''
# i = 1
# while len(strk) < k+1:
#     strk += str(i)
#     i += 1
#
# print(strk[k-1])
#
# 'Ответы: '
# '11 - 0'
# '35 - 2'
# '65011 - 5'
# '12345678 - 2'


# 2
# k = int(input())

# strk = []
# while True:
#     for i in range(0,12):
#         strk.append(i)
#
#     print(strk)


# a = int(input())
# res = round(a/3.14)
# print(int(res**0.5))
#


# y = 1000
# k = 7
# c = 0
# lst = []
# for i in range(1,1001):
#     lst.append(i)
#
# while len(lst) >= k:
#     c += 1
#     del lst[k - 1::k]
#
# print(c)


# # Задача 1
# # Код:
# a = int(input()) #1 точка во времени
# b = int(input()) #2 точка во времени
# new_str = bin(b-a) #разница между точками в двоичной сс
# #Получение 'чистой' строки
# j = new_str.index('b')
# new_str = new_str[j+1:]
#
# #Создание новых пустых переменных
# c_n = 0
# c_o = 0
# for i in new_str:
#     #нахождение кол-ва единиц
#    if i == '1':
#         c_n += 1
#     #нахождение общего кол-ва чисел
#    c_o += 1
# #Вывод результата
# print(c_o-c_n)


'''
Задача 2

2.1

Пусть масса меда и дегтя в ложке = 20 грамм и масса бочки = 2000 грамм

Тогда концентрация дегтя в бочке с медом = 20/(2000+20) = 0.00990099
а концентрация меда в той же бочке 1-(20/2020) = (2020-1)/2020

Содержание меда в ложке, которую взяли из бочки с медом после добавления дегтя
20*(2019/2020) = 19.8 гр

Значит, концентрация меда в бочке дегтя = 19.8/2000= 0.0099

Ответ: Концентрация дегтя в бочке с медом в которую положили деготь,
больше концентрации меда в бочке с дегтем на 0.00000099 гр

2.1
Пусть обьем бочки с дегтем в n раз больше бочки с медом,
С дегтем: n*2000
С медом: 2000

Концентрация дегтя в бочке с медом как в первом вопросе, = 0.00990099
А меда в дегте: 19.8/n*2000 = 0.0099/n , то есть в n раз меньше чем в одинаковых бочках

Обратный вариант:
с дегтем: 2000
с медом: n/2000

Концентрация дегтя в бочке с медом = 20/(n/(2000+20)) = 20/n/2020 = 1/n/101
Концентрация в n раз меньше чем в варианте с одинаковыи бочками

Содержание меда в ложке, которую взяли из бочки с медом после добавления дегтя
20*(100/n*101) = 19.8/n гр

Значит, концентрация меда в бочке дегтя = (19.8/n)/2000= 0.0099/n


Полный ответ:
2.1) Ответ: Концентрация дегтя в бочке с медом в которую положили деготь,
больше концентрации меда в бочке с дегтем на 0.00000099 гр
2.2)
1. Если бочка с дегтем будет в n раз больше бочки с медом,
то концентрация дегтя в бочке с медом не изменится, а концентрация меда
в бочке дегтя уменьшится в n раз
2. Если бочка с медом будет в n раз больше бочки с дегтем,
то концентрация дегтя в бочке с медом уменьштся в n раз и концентрация меда
в бочке дегтя уменьшится в n раз


Петеримов Александр
9 Мастерская

'''

# from math import log
#
# a = int(input())
# x = 0
# res =''
#
# lst = []
#
#
#
# for i in range(a):
#     lst.append(4**i)
#     if a - 4**i == 0:
#         res = f'{4}^{i}'
#     elif (a - 4**i) in lst:
#         p = a-4**i
#         x = log(p)/log(4)
#         res = f'{4}^{i} + {4}^{int(x)}'
#
# if res == '':
#     print('Это число невозможно представить в виде суммы степеней четверки')
# else:
#     print(res)


# Импортируем логарифмы
from math import log
#
# str = input().split()
# count = 0
# lst = []
# for i in str:
#     lst.append(int(i))
# while lst != []:
#     for i in range(len(lst) - 1):
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j - 1]:
#                 lst[j], lst[j - 1] = lst[j - 1], lst[j]
#
#         if lst[0] > 0:
#             lst[2] -= 1
#             lst[0] -= 1
#             count += 1
#         elif lst[0] == 0 and lst[2] > lst[1] and lst[1] > 0:
#             lst[2] -= 1
#             lst[1] -= 1
#             count += 1
#         elif lst[0] == 0 and lst[1] > lst[2] and lst[2] > 0:
#             lst[1] -= 1
#             lst[2] -= 1
#             count += 1
#
#
#         else:
#             break
#     if lst[0] == 0 and lst[1] == 0 or lst[1] == 0 and lst[2] == 0 or lst[2] == 0 and lst[0] == 0:
#         break
#
# print(count)
# print(lst)


# str = input().split()
# a = int(str[0])
# b = int(str[0])
# c = int(str[0])
# result = (a+b+c)//2
#
# print(result)


# while lst != []:
#     print(lst)
#     if lst[0] != 0:
#         lst[2] = lst[2] - 1
#         lst[0] -= 1
#         count += 1
#     elif lst[0] == 0 and lst[2] > lst[1] and lst[1] > 0:
#         lst[2] -= 1
#         lst[1] -= 1
#         count += 1
#     elif lst[0] == 0 and lst[1] > lst[2] and lst[2] > 0:
#         lst[1] -= 1
#         lst[2] -= 1
#         count += 1
#     elif lst[0] == lst[1] == lst[2]:
#
#     else:
#         break









# while lst != []:
#     if lst[2] > lst[1]:
#         lst[2] -= 1
#         lst[1] -= 1
#         count += 1
#         print(lst)
#     elif lst[2] == lst[1]:
#         lst[2] -= 1
#         lst[1] -= 1
#         count += 1
#
#     elif lst[2] < lst[1]:
#         lst[1] -= 1
#         lst[2] -= 1
#         count += 1
# print(lst)

# print(a*(a-1))















"""
# Обьяснения:
# При вводе 3 банок a b c
# у туриста есть 6 вариантов при которых он не открывает 2 одинаковые банки за день
# ab, ac, ba, bc, ca, cb

"""



#
# def fact(n):
#     if n > 0 :
#         return n*fact(n-1)
#     elif n == 0:
#         return 1
#
# n = int(input())
# print(fact(n))





# def fact(n):
#     count = 1
#     for i in range(1,n+1):
#         if n>0:
#             count *= i
#         elif n==0:
#             return 1
#     return count
# n = int(input())
# print(fact(n))
#






































