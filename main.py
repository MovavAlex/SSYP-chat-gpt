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

# a = int(input())#Принимаем на вход число
# x = 0 #Создаем пустую переменную
# res =''#Создаем переменную, в которую будем записывать результат
# lst = [] #Создаем список
#
#


# Импортируем логарифмы
# from math import log
#
#
# a = int(input())#Принимаем на вход число
# x = 0 #Создаем пустую переменную
# res =''#Создаем переменную, в которую будем записывать результат
# lst = [] #Создаем список
# for i in range(a):
#
#     lst.append(4**i) # Добавляем все четверки в степени в список
#    # Проверяем число
#     # Если число - и есть четверка в степени, то добавляем его в res и заканчиваем программу
#     if a - 4**i == 0:
#         res = f'{4}^{i}'
#    #Иначе:
#    #Если число состоит из суммы двух четверок в степени,    # то мы находим степень второй четверки и добавляем его в res
#     elif (a - 4**i) in lst:
#         p = a-4**i
#         x = log(p)/log(4) # нахождение степени второй четверки
#         res = f'{4}^{i} + {4}^{int(x)}'
# #Проверка на наличие результата
# if res == '':
#     print('Это число невозможно представить в виде суммы степеней четверки')
# else:
#     print(res)

#
# s = input().split('x')
# a = int(s[0])
# b = int(s[1])
# c = 0
# lst = []
# for i in range(a):
#     if a > b:
#         c += 1
#         a -= b
#     elif a < b:
#         c += 1
#         b -= a
#
#
# print(c+1)
# print(a*b)
#
#

# def tr(arr):
#     d = arr[0]-arr[1]
#     for i in range(2,len(arr)-2):
#         if arr[i-1]-arr[i] != d:
#             return False
#
# print(tr([6,1,0,4]))


#
# pre = 0
# a = int(input())
# count = 0
# lst = []
# new = 0
# for i in range(a):
#     if a % 2 == 0:
#         a //= 2
#         count += 1
#     else:
#        break
#
# for i in range(1,a+1):
#     if i%2 != 0:
#         lst.append(i)
#
# for i in lst:
#     if i == a:
#         pre = lst.index(a)
#
#
# res = pre * a
#
#
#
# print(count + res)
#

#
# a = 11
# nech = a-(a//2)
# chet = a//2
# print(nech)
# print(chet)



#
# a = input()
# res = ''
# for i in a:
#     if i == '(' and ')' in a:
#         res = 'Right'
#     elif i == '(' and ')' not in a:
#         res = 'Wrong'
#     elif i == '{' and '}' in a:
#         res = 'Right'
#     elif i == '{' and '}' not in a:
#         res = 'Wrong'
#     elif i == '[' and ']' in a:
#         res = 'Right'
#     elif i == '[' and ']' not in a:
#         res = 'Wrong'
# print(res)

# a = input()
# lefts = 0
# rights = 0
# Bracesleft = []
# Bracesright = []
# Square_bracketsleft = []
# Square_bracketsright= []
# Parenthesesleft = []
# Parenthesesright = []
#
# for i in a:
#     if i == '{':
#         Bracesleft.append(a.index(i))
#         lefts += 1
#     elif i == '}':
#         Bracesright.append(a.index(i))
#         rights += 1
#     elif i == '[':
#         Square_bracketsleft.append(a.index(i))
#         lefts += 1
#     elif i == ']':
#         Square_bracketsright.append(a.index(i))
#         rights += 1
#     if i == '(':
#         lefts += 1
#         Parenthesesleft.append(a.index(i))
#     elif i == ')':
#         rights += 1
#         Parenthesesright.append(a.index(i))
# print('{: ',Bracesleft)
# print('}: ',Bracesright)
# print('[: ',Square_bracketsleft)
# print(']: ',Square_bracketsright)
# print('(: ',Parenthesesleft)
# print('0: ',Parenthesesright)
# print(len(a))
# print(lefts,rights)

# if lefts > rights or lefts < rights:
#         res = 'Wrong'
# else:
#     for i in range(True):
#         if Bracesleft[i] > Bracesright[i] or Square_bracketsleft[i] > Square_bracketsright[i] or Parenthesesleft[i] > Parenthesesright[i]:
#             res = 'Wrong'
#             break
#         else:
#             res = 'Right'
#             break
#
# print(res)






a = input()
lst = []
open = '{(['
close = '})]'

err = 0


for i in a:
    if i in open and i == '(':
        lst.append(i)
    elif i in close and i == ')':
        try:
            lst.remove('(')
        except ValueError:
            print("Wrong")
            err = 1
            break
    elif i in open and i == '[':
        lst.append(i)
    elif i in close and i == ']':
        try:
            lst.remove('[')
        except ValueError:
            print("Wrong")
            err = 1
            break
    elif i in open and i == '{':
        lst.append(i)
    elif i in close and i == '}':
        try:
            lst.remove('{')
        except ValueError:
            print("Wrong")
            err = 1
            break






if lst == [] and err == 0:
    print('Right')
elif err == 1:
    print()
else:
    print('Wrong')














