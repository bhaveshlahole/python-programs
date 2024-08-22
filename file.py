                # FILE OPEN , READ
file = open("doc.txt", "r")
data = file.read()
print(data)
print(type(data))
file.close()
                # Reading file upto certain nuber

file = open("doc.txt","r")
data = file.read(5)
print(data)
file.close()
