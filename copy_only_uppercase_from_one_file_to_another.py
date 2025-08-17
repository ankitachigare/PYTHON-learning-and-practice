myfile2=open("info2.txt","w")
with open("info.txt") as myfile1:
    data=myfile1.read()
    for ch in data:
        if ch.isupper():
            myfile2.write(ch)
