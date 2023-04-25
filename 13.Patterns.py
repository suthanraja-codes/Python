# NUMBER PATTERN

# 1.

# for i in range (1,6):
#     for j in range (1,6):
#         print(1,end='')
#     print('')

# 2.

# for i in range(1,6):
#     for j in range(1,6):
#         if(i%2==1):
#             print(1,end='')
#         else:
#             print(0,end='')
#     print('')

# 3.

# for i in range(1,6):
#     for j in range(1,6):
#         if(j%2==1):
#             print(0,end='')
#         else:
#             print(1,end='')
#     print('')

# 4.

# for i in range(1,6):
#     for j in range(1,6):
#         if(i==3 & j==3):
#             print(0,end='')
#         else:
#             print(1,end='')
#     print('')

# 5.

# for i in range (1,6):
#     for j in range(1,6):
#         if((i==1) | (i==5) | (j==1) | (j==5)):
#             print(1,end='')
#         else:
#             print(0,end='')
#     print('')

# 6.

# for i in range(1,6):
#     for j in range(1,6):
#         if((i%2==1) & (j%2==1)):
#             print(1,end='')
#         elif((i%2==0) & (j%2==0)):
#             print(1,end='')
#         else:
#             print(0,end='')
#     print('')

# 6 . 2nd - model

# k = 1
# for i in range(1,6):
#     for j in range(1,6):
#         if(k==1):
#             print(1,end='')
#         else:
#             print(0,end='')
#         k=k*-1 #1*-1=-1
#     if(j%2==0):
#          k=k*-1
#     print('')

# 7.

# for i in range(1,6):
#     for j in range(1,6):
#         if(j==3) | (i==3):
#             print(0,end='')
#         else:
#             print(1,end='')
#     print('')

# 8.

# for i in range(1,6):
#     for j in range(1,6):
#         if((1<j<5)&(i==1)) | ((1<j<5)&(i==5)):
#             print(0,end='')
#         elif((i%2==0)&(j%2==1)):
#             print(0,end='')
#         elif((i==3)&(j!=3)):
#             print(0,end='')
#         else:
#             print(1,end='')
#     print('')

# 8. -secound model

# for i in range(1,6):
#     for j in range(1,6):
#         if((i==j)|(j==6-i)):
#             print(1,end='')
#         else:
#             print(0,end='')
#     print('')

# 9.

# for i in range(1, 6):
#     for j in range(1, 6):
#         if (i == 1 & j == 1) | (i == 1 & j == 5) | (i == 5 & j == 1) | (i == 5 & j == 5):
#             print(0, end='')
#         elif (i == 1) | (i == 5) | (j == 1) | (j == 5):
#             print(1, end='')
#         elif(i==5 & j ==1):
#             print(0,end='')
#         else:
#             print(0, end='')
#     print('')
