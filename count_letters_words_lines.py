wc=0
cc=0
cc1=0
with open("info.txt") as myfile:
    alllines=myfile.readlines()
    lc=len(alllines)
    print('Total number of lines are : ',lc)
    for line in alllines:
        for ch in line:
            cc+=1
        line=line.strip('\n')
        wordlist=line.split(" ")
        wc=wc+len(wordlist)
        for word in wordlist:
            cc1=cc1+len(word)
    
    print('Total words : ',wc)
    print('Total characters with space : ',cc)
    print('Total characters without spaces : ',cc1)
