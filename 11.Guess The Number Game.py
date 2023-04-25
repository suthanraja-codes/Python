# import random
#
# num = random.randint(1,20)
#
# guess = int(input("Enter The Number : "))
# attempts = 0
# while num!=guess:
#     if attempts <= 2:
#         if num<=guess:
#             print("You Entered The Number Is higher")
#         else:
#             print("Enter The Number Is Lower")
#         guess = int(input("Guess Again..."))
#         attempts+=1
#     else:
#         print("Game Over")
#         break;
# if num==guess:
#     print("won")

def add(*k):
    sum = 0
    for i in k:
        sum = sum + i
    print(sum)

add(1,2,3,4)