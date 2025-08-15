print('Example 1')
myfile=open("info.txt","r")
data=myfile.read()
print(data)
myfile.close()

print('Example 2')
myfile=open("info.txt","r")
for lines in myfile:
    print(lines)
myfile.close()

print('Example 3')
myfile=open("info.txt","r")
alllines=myfile.readlines()
for line in alllines:
    print(line)
myfile.close()

print('Example 4')
with open("info.txt") as myfile:
    data=myfile.read()
    print(data)
myfile.close()

print('Example 1')
with open("info.txt","w") as myfile:
    myfile.write("hello!!!\n")
    myfile.write("We are learning python.\n")
myfile.close()

print('Example 2')
myfile=open("info.txt","w")
lines=['java\n','python\n','cpp\n','php\n']
myfile.writelines(lines)

myfile.close()
