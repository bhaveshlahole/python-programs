"""
start = "hi welcome"
print(start.endswith("me"))
print(len(start))
"""
            #conditional statememts {IF ELIF}

"""
marks = float(input("Enter your marks"))
if(marks >= 90):
    print("A grade")
elif(marks >= 80 and marks < 90):
    print("B grade")
elif(marks >= 70 and marks  < 80):
    print("c grade")
elif(marks >= 60 and marks  < 70):
    print("d grade")
else:
    print("Fail")
  """

            #conditional statements {NESTING OF IF ELSE STATEMENT}
"""
age = float(input("Enter the age of canditates"))
if(age >= 18):
    if(age >= 80):
        print("Not permitted to drive")
    else:
         print("Can drive")
else:         
    print("can not drive")
"""
            # EVEN OR ODD NUMBER CHECKER
"""
num = int(input("Enter even or odd number"))

if( num %3 == 0 ):
    print("Entered number is even")

else:
    print("Entered number is odd")
"""

          # GREATEST OF THREE NUMBERS
"""
a = int(input("Enter value for a numbers"))
b = int(input("Enter value for b numbers"))
c = int(input("Enter value for c numbers"))
#a,b,c = 24,28,68
if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is graetest")
"""
                #CHECKING FOR MULTIPLE OF 7
"""
seven = float(input("Enter the number of your desire"))
if( seven %7 == 0):
    print("Enterd number is multiple of seven")
else:
    print("Entered number is not multiple of seven")
"""

                # LISTS AND IT'S OPERATION IN  PYTHON
"""                              
student = ["BHAVESH",34,"C2","Amravati"]
print(student)
print(student[0])
student[0]= "TAPPU"
print(student)

marks = [35,40,42,44,46,48,50]
print(marks[2:5])
print(marks[-4:-1])
print(marks.sort(reverse = True))
print(marks)
"""
                                          # APPEND IN PYTHON LIST
"""
                                         
list = []
fav1 = str(input("Enter your three favourate movies"))
fav2  = str(input("Enter your three favourate movies"))
fav3 = str(input("Enter your three favourate movies"))
list.append(fav1)
list.append(fav2)
list.append(fav3)
print(list)

"""
