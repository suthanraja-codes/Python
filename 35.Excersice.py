l = [1, 5, 8, 2, 7]

count = 0

for i in (l):
    #     print( " values " , i)
    count += 1
#     print(count)
for i in range(count):

    # print("--------------")

    print(i)

    # print("--------------")

    for j in range(count - 1):

        # print("--------------")

        # print(j)

        # print("--------------")

        # print(l[j], "<", l[j + 1])

        # print(l[j] < l[j + 1])

        # print("-------------------------")

        if l[j] < l[j + 1]:
            # print(l[j], " < ", l[j + 1])

            # print(" A -------------------------")

            l[j], l[j + 1] = l[j + 1], l[j]

            # print(l[j], l[j + 1], "=", l[j + 1], l[j])

            # print(" B -------------------------")

    print(l)

    # print(" C -------------------------")

print(l)

