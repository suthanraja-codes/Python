
                                                # Map
                                    # Map (Function , Iterable)

                                            # Inr To Usd
# items =[(3456,"shoe",780),(3566,"phone",25300),(2587,"book",450),(5412,"pen",75)]
# inr_usd = lambda item : (item[0],item[1],float("{:.2f}".format(item[2]/74)))
# inr_usd_map = list(map(inr_usd,items))
# print(inr_usd_map)
#
#
#                                             # Average
# students = [("maths","anitha",452),("biology","anand",412),("biology","balaji",185),("maths","chandru",390)]
# avg = lambda stu : (stu[1],float("{:.2f}".format(stu[2]/5)))
# average = list(map(avg,students))
# print(average)

                                            # Question - 1
# Students = [("Maths","Anitha",180),("Biology","Anand",182),("Biology","Balaji",170),("Maths","Chandru",190)]
# # Create Another list and marks for 100
#
# create =  lambda item : (item[1],float("{:.2f}".format(item[2]/2)))
# crt = list(map(create,Students))
# print(crt)

                                            # Question - 2

val = [72,78,99,12,56]
# Expect Result - ['even', 'even', 'odd', 'even', 'even']
odd_even = lambda odd : "even" if (odd%2==0) else "odd"
even = list(map(odd_even,val))
print(even)