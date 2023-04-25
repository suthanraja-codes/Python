l = [67,28,19,2]
li = []
while l:
    min = l[0]  # 67
    for i in l:
        # print(i,min)
        if i < min:  # 67 < 67
            # print(min, i)
            min = i
            # print(min)
    # print(min, i)
    li.append(min)  # 2
    # print(li)
    l.remove(min)# 2
    # print(l)
print(li)
