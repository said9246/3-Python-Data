# filehangling 


# file =open("sample.txt","w")
# file.write("Hello, this is a sample text file.")
# file.close()

# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("sample.txt", "a")
# file.write("This is an additional line.")
# file.close()

file =open("sample2.txt","x")
file.write("Helo this is orignal data ok  .")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()