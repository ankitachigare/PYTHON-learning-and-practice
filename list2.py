list=[22,33,44,'hello',3.4,'php',True]
i=0
print('[',end=' ')
while i<len(list)-1:
    if type(list[i]) is str:
        print('\'',list[i],'\'',end=' , ',sep=' ')
    else:
        print(list[i],end='$ ')
    i+=1
print(list[i],end=' ')
print(']')