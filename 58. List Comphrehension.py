
                                            # List Comphrehension
                                # To Create a new list from exisiting list

                                # list = [expression for item in iterable]

                                                # Qn - 1
                                # List Of Square in first 10 natural Number

# natural = [x*x for x in range (1,11)]
# print(natural)
#
# # Map
#
# natural1 = list(map(lambda x:x*x,range(1,11)))
# print(natural1)

                                                # Qn - 2
                                # list = [expression for item in iterable if condition]

# temp = [28,30,25,38,22,31]
# temp_filter = [i for i in temp if i<30]
# print(temp_filter)

                                                # Qn - 3
                                # list = [expression if - else for item in iterable]

temp = [28,30,25,38,22,31]
temp_filter = [i if i<30 else 0 for i in temp]
print(temp_filter)