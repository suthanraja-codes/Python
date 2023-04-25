# a = 10
# b = 20
#
# if a > 0 and b >10:
#     print ("suthan")
# if (a > 0 &     b>10) :
#     print ("raja")

def binary(num):
    if num >= 1:
        print(num % 2)
        binary(num // 2)
num = int (input("Enter : "))
binary(num)