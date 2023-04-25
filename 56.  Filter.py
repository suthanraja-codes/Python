
                                                # Filter
                                      # Filter(Function , Iterable)
            # Function Should Return True Or False, If True , the item will be added to result , if false omitted.

                                                    # Qn - 1
# Less Than 500
# items =[(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
# filtering = lambda l : l[2] > 500
# filtered = list(filter(filtering,items))
# print(filtered)


                                                    # Qn - 2
# items =[(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
# filtered = list(filter(lambda l : l[1][0] == 'p',items))
# print(filtered)


                                                    # Qn - 3

# items =[(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
# filitered = list(filter(lambda l :  4000 > l[0] > 3000,items))
# print(filitered)

                                                    # Qn - 4
# students = [("maths","Anitha",180),("biology","Anand",182),("maths","chandru",192)]
# filtered = list(filter(lambda l : l[1][0]=='A',students))
# print(filtered)

                                                    # Qn - 5
students = [("maths","Anitha",180),("biology","Anand",182),("maths","chandru",192),("biology","balaji",170)]
filtered = list(filter(lambda l : l[2]>=180,students))
print(filtered)