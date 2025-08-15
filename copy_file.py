myfile1=open("info.txt","r")
myfile2=open("info2.txt","w")

data=myfile1.read()
myfile2.write(data)

myfile1.close()
myfile2.close()