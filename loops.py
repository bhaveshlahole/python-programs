                     # while loop 
"""              
count = 0
while count <= 20:
    count += 2.00001
    print(count)
"""
                    # While loop to print  1 to 100
"""
nums = 1
while nums <= 100 :
    print(nums)
    nums += 1
    """
                    # While loop to print 100 to 1

"""
nums = 100
while nums >= 1:
    print(nums)
    nums -= 1
"""

                    # print the multiplication table of number n
"""
n = int(input("Enter the Table you want" ))
i = 1
while i<= 10: 
    print(n*i)
    i+= 1
"""
                 # Printing index of list
"""
nums = [1,4,9,16,25,36,49,64,81,100]
indx = 0
while indx < len(nums):
    print(nums[indx])
    indx += 1
"""
                 # Finding values in tuples (PROBLAMETIC BUT HANDLED BY BREAK)
"""
nums = (1,4,9,16,25,36,49,64,81,100,36)
#x = int(input("Enter number to find in list"))
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x ):
        print("Found at indx",i)
        break
    else:
        print("Finding")
    
        i += 1
"""

                          # USE OF CONTINUE WORD IN PYTHON
                           #(UNCERTAINITY IN THE BELOW PROGRAM)
"""
i = 1
while i<= 10:
    if(i%2 == 0):
        i += 1
        continue
        print(i)
        i += 1
"""

                   # FOR LOOP
"""
man = ["Ironman","spiderman","Batman ","Superman"]
for heros in man:
    print(heros)
"""
"""
num = (1,4,3,16,25,36,49,64,81,100,49)
x = 100
idx = 0
for el in num:
    if(el == x):
        print("Number found at idx",idx)
        idx += 1   
"""


              # RANGE FUNCTION

"""
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

for i in range(2,100,2):
    print(i)

for i in range(100,0,-1):
    print(i)

"""
                   # TABLE USING FOR AND RANGE 
"""
n = int(input("Enter number you want to form table"))
for i in range(1,11):
    print(n*i)
"""

                      # sum of n natural numbers

"""
n = 10
sum = 0
for i in range(1,n+1):
    sum += i

print("Sum of number is",sum)
"""

                          #Factorial
"""
n  = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

    
print("Total sum is:",fact)

x = 6
fact = 1
for i in range (1,x+1):
    fact *= i

print("Factorial is ",fact)

 """         
               

                      



































