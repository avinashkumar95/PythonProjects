name=[]
phnumber=[]
address=[]
while True:
    name.append(input("Enter Name: ").upper())
    phnumber.append(input("Enter PhoneNumber: "))
    address.append(input("Enter Address: ").upper())
    print("Added Successfully")
    if(input("Want to Retrive?(YES/NO):: ").upper() == "YES"):
        i=name.index(input("Enter to be search name: ").upper())
        print("Search Found")
        print("Name: "+name[i]+" Phone Number: "+phnumber[i]+" Address: "+address[i])
    if(input("Want to add More?(YES/NO):: ").upper() == "YES"):
        continue
    else: break