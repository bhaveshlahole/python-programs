                # RECURSIVE FUNCTION
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5) 

                   # RECURSIVE FUNCTION FOR FACTORIAL OF NUNBERS

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n - 1)*n
print("Factorial of input is:",fact(4))

                    # RECURSIVE FUNCTION TO CALCULATE SUM

def calc_sum(n):
    if(n == 0):
        return
    print(n)
    calc_sum(n-1)

calc_sum(5)    

                   # RECURSIVE FUNCTION 
