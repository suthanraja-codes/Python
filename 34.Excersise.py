# #                                                 SORT
#
# l = [2, 8, 4, 0, 5]
# count = 0
# #
# for i in l:
#     count = count + 1
# print(count)


#                                            ASCENDING ORDER


# for j in range (count):
#     # print("l[j] ",l[j])
#     for i in range(count-1):
#         # print("l[i] ",l[j]," - ",l[i])
#         if l[i] > l[i + 1]: # 2 < 8 , 8 < 4 , 4 < 0 , 0 < 5
#             # print("l[i] " ,l[i], " == ",l[i+1])
#             l[i], l[i + 1] = l[i + 1], l[i] # [8,2,4,0,5] [8,2,4,5,0]
#              # print(l)
# print(l)
# #

#                                           DESENDING ORDER


# for j in range (count):
#     for i in range(count - 1):
#         if l[i] < l[i + 1]: # 2 < 8 , 8 < 4 , 4 < 0 , 0 < 5
#             l[i], l[i + 1] = l[i + 1], l[i] # [8,2,4,0,5] [8,2,4,5,0]
#             # print(l)
# print(l)


# n = 5
# position = 1
# while(n):
#     x = input("Enter : ")
#     print(position," ",x)
#     position+=1

#           Extend,

# a = [1,2,3,4,5]
# l = []
# count = 0
# index = int(input("Enter The Index : "))
# value = input("Enter The Value : ")
# # li = list(value)
# for i in a:
#     count+=1
# for j in  value:
#     l+=j
#     # print(l)
# if(count < index):
#     a+=l
#     # print(a)
# print(a)


#                                       HOLLOW PATTERNS

'''
                                        * * * * * 
                                                  
                                                  
                                                  
                                        * * * * * 

'''
# n = int(input("Enter The Value : "))
# for i in range(n):
#     for j in range (n):
#         if(i==0 or i==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
                            *              *  
                            *              *  
                            *              *  
                            *              *  
                            *              *  

'''
# n = int(input())
# for i in range(n):
#     for j in range (n):
#         if(j==0 or j==n-1):
#             print("* ",end=" ")
#         else:
#             print("   ",end=" ")
#     print()

'''
                            * 
                            * * 
                            *   * 
                            *     * 
                            * * * * * 

'''

# n = int(input( ))
# for i in range(n):
#     for j in range (i+1):
#         if(i==n-1 or j==0 or i==j):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input())
# for i in range (n):
#     for j in range (i+1):
#         print(" ",end=" ")
#     for k in range (i,n):
#         print("*",end=" ")
#     print()


'''
                                * * * * * 
                                *     * 
                                *   * 
                                * * 
                                * 
'''
# n = int(input())
# for i in range (0,n):
#     for j in range (i,n):
#         if(i==0 or i==j or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#


'''
                                      * 
                                    *   * 
                                  *       * 
                                *           * 
                              * * * * * * * * *  
  
'''

'''

n = int(input("Enter The Number : "))
for i in range (n):
    for j in range (i,n):
        print(" ",end=" ")
    for u in range (i+1):
        if(u==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range (i):
        if(i==n-1 or k==i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''

