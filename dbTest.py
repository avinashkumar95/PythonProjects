import sqlite3 as sql
import random
def Delete_Table(x):
    try:
        conn=sql.connect("TestDB")
        query = """DROP TABLE """+x
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except:
        print("ERROR OCCUR WHILE DROP TABLE")
    finally:
        conn.close()

def Insert_Table(id,name,phone,address):
    try:
        conn = sql.connect("TestDB")
        query = """INSERT INTO testDB VALUES(?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(query, (id, name, phone, address))
        conn.commit()
        print("Item Inserted to testDB")
    except:
        print("ERROR OCCUR WHILE INSERTING")
    finally:
        conn.close()

def Create_TableID():
    try:
        conn = sql.connect("TestDB")
        query = """CREATE TABLE IF NOT EXISTS testDB(
                    ID integer PRIMARY KEY,
                    NAME text NOT NULL,
                    PHONE,
                    ADDRESS)"""
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("Table Created testDB")
    except:
        print("ERROR WHILE CREATING")
    finally:
        conn.close()

def Create_TableItem(x):
    try:
        conn = sql.connect("TestDB")
        query = """CREATE TABLE IF NOT EXISTS TokenID"""+x+"""
                (Name,
                Phone,
                Address,
                Item,
                Price)"""
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("Item Table Created TokenID"+x)
    except:
        print("Error in Creating Item Table")
    finally:
        conn.close()

def Insert_TableItem(x,name,phone,address,grocery_Item,price):
    try:
        conn = sql.connect("TestDB")
        query = """INSERT INTO TokenID"""+x+""" VALUES (?,?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(query, (name,phone,address,grocery_Item,price))
        conn.commit()
        print("Item Inserted to TokenID"+x)
    except:
        print("Error in insert to itemTable")
    finally:
        conn.close()

def sumItemTable(x):
    try:
        conn = sql .connect("TestDB")
        query = """SELECT SUM(price) FROM TokenID"""+x
        cur = conn.cursor()
        cur.execute(query)
        total_price = cur.fetchall()
        #conn.commit()
    except:
        print("Error in getting Sum")
    finally:
        conn.close()
        return total_price


Create_TableID()
while 1:
    x = random.randint(1000, 10000000)
    name = input("Enter Name::")
    phone = input("Enter Phone Number::")
    address = input("Enter Address::")
    Insert_Table(x, name, phone, address)
    op = input("Want to Purchase Something?(y/n):: ")
    if(op=="y"):
        Create_TableItem(str(x))
        while 1:
            grocery_Item = input("Enter Item:: ")
            price = float(input("Price:: "))
            Insert_TableItem(str(x),name,phone,address,grocery_Item,price)
            op2 = input("More Item?(y/n):: ")
            if(op2=="n"):
                TotalPrice= sumItemTable(str(x))
                print("Total Price = $"+str(TotalPrice))
                break
        op = input("More Customer(y/n)?:: ")
        if(op=="Y"):
            continue
        else:
            break
    else:
        break


#Insert_Table(random.randint(1000,1000000),"SHARIQ","29474462***","Something Else")
#Insert_Table(random.randint(1000,1000000),"BALAJI","27466565***","Something Else")
#Delete_Table("TokenID100")

#Create_TableItem(str(100))
#Insert_TableItem(str(100),"Avinash","2166819555","Something","apple","5.00")
#Insert_TableItem(str(100),"Avinash","2166819555","Something","grapes","10.00")
#print(sumItemTable(str(100)))