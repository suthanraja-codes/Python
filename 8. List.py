districts = ["Tirunelveli", "Thoothukudi", "Tenkasi", "Kanniyakumari", "Coimbatore"]
numbers = [12, 83, 1, 38, 16]

# ADDING ELEMENTS
# Insert
districts.insert(3, "Chennai")
print(districts)

# Append
districts.append("Selam")
print(districts)

# Extend
districts.extend(["Ramanathapuram", "Madurai"])
print(districts)

# DELETING ELEMENTS
# DEL
del districts[3]
print(districts)

# Pop
districts.pop()
print(districts)

# pop using index
districts.pop(1)
print(districts)

# remove - using for particular value name
districts.remove("Selam")
print(districts)

# INFORMATION
# index
x = districts.index("Tirunelveli")
print(x)

# count
y = districts.count("Tirunelveli")
print(y)

# #MODIFING
# #sort
# districts.sort()
# print(districts)
#
# #reverse
# districts.reverse()
# print(districts)


# LIST FUNCTIONS
# len

print(len(districts))

# min
print(min(numbers))

# max
print(max(numbers))

# sum
s = sum([1, 2, 3])
print(s)

q = sum((1, 2, 3))
print(q)

w = sum({1, 2, 3})
print(w)

# sorted - temproary sorted
print(sorted(numbers))

# #reversed - temproary reversed
# r=reversed([q,w])
# print(r)
