ucnt=0
cnt=0
myfile=open("info.txt","r")
data=myfile.read()
for ch in data:
    cnt+=1
    if ch.isupper():
        ucnt+=1

print('Total number of charaters : ',cnt)
print('Total number of uppercase charaters : ',ucnt)
