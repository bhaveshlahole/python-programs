import random
import string

pass_len = 12
charValues = string.punctuation + string.digits + string.ascii_letters 

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your password is:",password)
