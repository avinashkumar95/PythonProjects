while True:
    x=input("Enter Password for Validation:: ")
    isDigit=isUpper=isLower=False
    if(len(x)>=8):
        for i in x:
            if(i.isdigit()):    isDigit=True
            if(i.isupper()):    isUpper=True
            if(i.islower()):    isLower=True
        if((isDigit) and (isLower) and (isUpper)):
            print("Valid Password")
            break
        else: print("Invalid Password")