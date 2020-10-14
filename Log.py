def addLog(op,a,b,output):
    f=open("LogFile.txt",'a')
    f.writelines(op+"\t\t"+a+","+b+"\t\t"+output+"\n")
    f.flush()
    f.close()

def headers():
    f = open("LogFile.txt","w")
    f.writelines("Operation"+"\t\t"+"Inputs"+"\t\t"+"Outputs"+"\n")
    f.flush()
    f.close()

def operation(a,b,op):
    if op=="+":
        x=a+b
        addLog("Addition",str(a),str(b),str(x))
        print(x)
    elif op=="-":
        x=a-b
        addLog("Difference",str(a),str(b),str(x))
        print(x)
    elif op=="*":
        x=a*b
        addLog("Multiply",str(a),str(b),str(x))
        print(x)
    elif op=="/":
        x=a/b
        addLog("Division",str(a),str(b),str(x))
        print(x)
    elif op=="%":
        x=a//b
        addLog("Modulus",str(a),str(b),str(x))
        print(x)
    else:
        print("***Wrong Choice Enter***")
        operation(a,b,input("Enter Correct Operation:: "))


headers()
while True:
    operation(int(input("Enter first number: ")),int(input("Enter second number: ")),input("Enter Operation: "))
    if(input("Want to Continue?(y/n)")=="n"):
        break





