content=''
myfile=open("info.txt","r")
data=myfile.read()
for ch in data:
    content= content + ch + '@'
myfile.close()
print(content)