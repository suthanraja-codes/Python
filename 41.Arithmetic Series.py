#                       ARITHMETIC SERIES

#                      1.  1+2+3+4.....N

'''

sum = 0
a = 1
n = int(input("Enter N value : "))
for i in range(1,n+1):
    sum = sum + a
    a+=1
print("Sum Of The Series = ",sum)

'''
#                     2. 9 + 13 + 17 + ..... N

'''
sum = 0
a = 9
n = int(input("Enter N Value : "))
for i in range (1,n+1):
    sum += a
    a+=4
print("Sum Of The Series is ",sum)

'''
#                   3. 2+4+6+8....N


'''

sum = 0
a = 2
n = int(input("Enter N value : "))
for i in range (1,n+1):
    sum = sum+a
    a+=2
print("Sum Of The Series ",sum)
'''



#                   4.1+3+5+7....N

'''
sum = 0
a = 1
n = int(input("Enter N Value : "))
for i in range(1,n+1):
    sum = sum + a
    a+=2
print("Sum Of The Series ",sum)

'''

#                  5.10+9+8+7....+1

sum = 0
a=10
n=int(input("Enter N value : "))
for i in range (1,n+1):
    sum+=a
    a-=1
print("Sum Of The Series ",sum)