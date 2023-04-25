
# a = [7,1,2,3,4,5,6]
# a.sort()
# print(a)
# i = 0
# n = len(a)
# print(n)
# j = n-1
# while(i<j):
#     print(a[j] ,  end = ' ')
#     print(a[i], end = ' ')
#     j-=1
#     i+=1
# if(n%2!=0):
#     print(a[i])


a = [1 ,3 ,4 ,5]
b = [2, 4, 6, 8]
c = len(a)
d = len(b)
e = []
i,j=0
while(i<c & j<d):
    if(a[i] < b[j]):
        e.append(a[i])
    else:
        e.append(b[j])







