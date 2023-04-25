#Get input a number  n from user. print all the factors of n.

# n = int(input("Enter The Number : "))
# for i in range (1,n+1):
#     if(n%i)==0:
#         print(i ," is Factor")

#Get a list fo to do tasks from the user and add it to a to_do list.print list python
# li = []
# package = 0
# while package<=2:
#     name = input("Enter Your Name : ")
#     age = int(input("Enter The age : "))
#     bg = input("Enter Your Blood Group : ")
#     package+=1
#     li.append(name)
#     print(li)
#     print("[",name,age,bg,"]")

#Given an array of integers . find a peak element in it. an array element is a peak if it is not smaller than its neighbours.for corner elements , we need to consider only one neigbour.

numbers = [3,4,5,7,6]
length1 = len(numbers)
for i in range (length1):
    if (i >= numbers[i]):
        print(i)

