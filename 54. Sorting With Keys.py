
                                            # List Of Tubles

# Sorting With Keys

students = [("maths","anitha",80),("biology","anand",82),("biology","balaji",72),("maths","chandru",90)]
# marks
students.sort(key =  lambda item:item[2])
print(students)

# name
students.sort(key = lambda item:item[1])
print(students)

# class
students.sort(key = lambda item:item[0])
print(students)

                            #               Tuble Of Tuble
students = (("maths","anitha",80),("biology","anand",82),("biology","balaji",72),("maths","chandru",90))
# class
print(sorted(students,key = lambda item : item[2]))
print(students)




