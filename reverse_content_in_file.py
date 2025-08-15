# print('Example 1')
# myfile=open("info.txt","r")
# data=myfile.read()
# revdata=data[::-1]
# print(revdata)
# myfile.close()

print('Example 2')
cnt=0
with open("info.txt") as myfile:
    for line in myfile:
        cnt+=1
        revline=line[::-1]
        print(cnt,' : ',revline)
