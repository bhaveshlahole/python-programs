"""a = 50
b = 20
print(a == b)
print(a != b)
                      # assignment operator
num = 28
#num = num + 2
num += 2
print(num)

sub = 30
sub -= 2
print(sub)

num *= 2
print(num)

print( not(num > sub))
                     #input from user

z = int(input("Enter value for z: "))
y = int(input("Enter value for y :"))
        

print("sumation of z and y is :",z + y)

side = float(input("Enter the side of square for area calculation: "))
print(side ** 2)"""

                       #practice question

"""
num1 = float(input("Enter value for number 1 : "))
num2 = float(input("Enter value for number 2 : "))
if(num1 >= num2):
    print("True")

else:
    print("False")
    """
"""
print(num1 >= num2)

import sys
print(sys.version)
"""
                       # PALENDROMIC SEQUENCE
"""
list1 = [1,2,3,2]
#list2 = [2,3,4,5,6]

#list1.append(input("Enter list here"))
list1_copy = list1.copy()
list1_copy.reverse()
if(list1_copy == list1):
    print("Palendrome")
else:
    print("Not palendrome")
"""

                        #TUPPLES PROBLEM

grade = ("A","C","D","A","B", "A")
print(grade.count("A"))
grade = ["A","C","D","A","B", "A"]
grade.sort()
print(grade)

