f=open("Words.txt","r")
count=0
countAll=0
checkList=["in","on","an","the","am"]
for x in f:
    z=x.split(' ')
    for i in z:
        if(i not in checkList):
            count = count+1