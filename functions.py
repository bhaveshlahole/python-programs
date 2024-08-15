           # CREATING A FUNCTION IN PYTHONS

"""def myfunc(num1,num2):
    sum = num1 + num2
    return sum

ler = myfunc(27,32)
print(ler)
"""
             # CALCULATING AVERAGE OF TWO NUMBERS
"""
def average(a,b,c):
    av = a+b+c/3
    return av
calc = average(22,3,5)
print(calc)
"""

                # LIST IN FUNCTIONS
"""
cities = ["delhi","mumbai","pune","chennai",]

def print_len(lists):
    print(len(lists))

print_len(cities)

"""
              # FACTORIAL OF A NUMBER
"""             
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

fact(9)
"""

            # CONVERSION OF INR RS TO USD

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"US =",inr_val,"INR")

    convert(73)
