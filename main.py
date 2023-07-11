
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







#2
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




y = 1000
k = 7
c = 0
lst = []
for i in range(1,1001):
    lst.append(i)

while len(lst) >= k:
    c += 1
    del lst[k - 1::k]

print(c)