##Развернуть строку
# a = 'LOLABC'
# n = []
# for i in range(len(a)-1,-1,-1):
#     n.append(a[i])
#
# new_str = ''.join(n)
# print(new_str)


##Паллиндромность
# a = input().upper()
# if a == a[::-1]:
#     print('pallindrome')
# else:
#     print('no pallindrome')
##Без срезов
# new = ''
# for i in range(len(a)-1,-1,-1):
#     new += a[i]
# if a == new:
#     print('pallindrome')
# else:
#     print('no pallindrome')




# a = '010011"0"000101'
# new = list(a)
# print(new)
# g = []
# for i in new:
#     if i != '0':
#         h = a[:i]
#         j = h.count('0')
#         g.append(j)
#
# print(g)



## new = [1,2,1,3,1]

# def func(a):
#     j = 0
#     c = 0
#     new = []
#     while c < 1:
#         for i in a:
#             if i == '0':
#                 j += 1
#                 new.append(j)
#             elif i != '0':
#                 a = a[j:]
#                 c += 1
#                 return func(a)
#
#     return new
# print(func(a))




##Нули и единицы
# a = '0100111000101'
# a = a.split('1'); print(a)
# print(len(max(a)))


##Капибара

# 5 3
# 5 5
# 5 4
# 1 3
# 2 4
# 5 1









#
# bi = input().split()
# n = int(bi[0])
# k = int(bi[1])
# lst = []
# nums = []
# for i in range(n):
#     a = input().split()
#     j = a[0] + a[1]
#     lst.append(int(j))
#     nums.append(i)
# while True:
#     for x in lst:
#         if x == min(lst):
#             # nums.pop(lst.index(x))
#             # # lst.remove(x)
#             k-=1
#             print(x)
#         elif x == max(lst):
#             # nums.pop(lst.index(x))
#             # # lst.remove(x)
#             k -=1
#             print(x)
#     if k == 0:
#         break
#
# print(nums)
# print(lst)



# bi = input().split()
# n = int(bi[0])
# k = int(bi[1])
# lst = []
# for i in range(n):
#     a = input().split()
#     a[0] = int(a[0])
#     a[1] = int(a[1])
#     lst.append(a)
# print(lst)
# lst.sort()
# print(lst)





#
# lst = [1,2,1,1,2,1]
# lst = [6,3,3,3,1,10,4,2]
# full = sum(lst)
# if full % 2 == 0:
#     for i in range(1, len(lst)):
#         if full / sum(lst[:i]) == 2:
#             print(i-1)
#
# else:
#     print('Нечетное')













# count = 0
#
# a = 100125
# N = len(a)
# lst = [5000, 1000, 500, 200, 100, 50, 20, 10, 5]
#
# for i in lst:
#     count += a // i
#     a = a%x
#
#
#
#
#
# print('Ответ: ', count)
#











#
#
#
# def bubble(a):
#     swap = True
#     while swap == True:
#         swap = False
#         for x in range(len(a)-1):
#             if a[x+1] < a[x]:
#                 a[x], a[x+1] = a[x+1], a[x]
#                 swap = True
# a = [-1, 18, 5, 7, -15, -2, 27]
# bubble(a)
# print(a)




#
# a = input().split()
#
# for i in range(len(a)):
#     print(i+1,1,2)
#     a = a[::-1]
#
# print('-----------then---------')
#
# for i in range(len(a),0,-1):
#     print(i,2,3)







