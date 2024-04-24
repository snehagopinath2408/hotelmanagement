import os
import platform
import mysql.connector
import pandas as pd
import datetime

global z
mydb = mysql.connector.connect(user='root', password='1234', host='localhost', database='hotel')
mycursor = mydb.cursor()

def registercust():
    L = []
    name = input("enter name:")
    L.append(name)
    addr = input("enter address:")
    L.append(addr)
    indate = input("enter check in date:")
    L.append(indate)
    outdate = input("enter check out date:")
    L.append(outdate)
    cust = (L)
    sql = "insert into custdata(custname,addr,indate,outdate)values(%s,%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()

def roomtypeview():
    print("Do you want to see room type available : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from roomtype"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

def roomrent():
    print("We have the following rooms for you:-")
    print("1. type A---->rs 1000 per night")
    print("2. type B---->rs 2000 per night")
    print("3. type C---->rs 3000 per night")
    print("4. type D---->rs 4000 per night")
    x = int(input("Enter Your Choice Please->"))
    n = int(input("How many nights did you stay:"))
    if x == 1:
        print("you have opted for room type A")
        s = 1000 * n
    elif x == 2:
        print("you have opted for room type B")
        s = 2000 * n
    elif x == 3:
        print("you have opted for room type C")
        s = 3000 * n
    elif x == 4:
        print("you have opted for room type D")
        s = 4000 * n
    else:
        print("please choose a room")
    print("your room rent is =", s, "\n")

def restaurantmenuview():
    print("Do you want to see the available menu: Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from restaurant"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)

def orderitem():
    global s
    print("Do you want to see the available menu : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from restaurant"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
    print("do you want to purchase from above list: enter your choice:")
    d = int(input("enter your choice:"))
    if d == 1:
        print("you have ordered tea")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for tea is :", s, "\n")
    elif d == 2:
        print("you have ordered coffee")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for coffee is :", s, "\n")
    elif d == 3:
        print("you have ordered cold drink")
        a = int(input("enter quantity"))
        s = 20 * a
        print("your amount for cold drink is :", s, "\n")
    elif d == 4:
        print("you have ordered samosa")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for samosa is :", s, "\n")
    elif d == 5:
        print("you have ordered sandwich")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for sandwich is :", s, "\n")
    elif d == 6:
        print("you have ordered dhokla")
        a = int(input("enter quantity"))
        s = 30 * a
        print("your amount for dhokla is :", s, "\n")
    elif d == 7:
        print("you have ordered kachori")
        a = int(input("enter quantity"))
        s = 10 * a
        print("your amount for kachori is :", s, "\n")
    elif d == 8:
        print("you have ordered milk")
        a = int(input("enter quantity"))
        s = 20 * a
        print("your amount for kachori is :", s, "\n")
    elif d == 9:
        print("you have ordered noodles")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for noodles is :", s, "\n")
    elif d == 10:
        print("you have ordered pasta")
        a = int(input("enter quantity"))
        s = 50 * a
        print("your amount for pasta is :", s, "\n")
    else:
        print("please enter your choice from the menu")

def laundrybill():
    global z
    print("Do you want to see rate for laundry : Enter 1 for yes :")
    ch = int(input("enter your choice:"))
    if ch == 1:
        sql = "select * from laundry"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for x in rows:
            print(x)
    y = int(input("Enter Your number of clothes->"))
    z = y * 10
    print("your laundry bill:", z, "\n")
    return z

def lb():
    print(z)

def res():
    print(s)

def viewbill():
    a = input("enter customer name:")
    print("customer name :", a, "\n")
    print("laundry bill:")
    lb()
    print("restaurant bill:")
    res()

def Menuset():
    print("enter 1: To enter customer data")
    print("enter 2 : To view roomtype")
    print("enter 3 : for calculating room bill")
    print("enter 4 : for viewing restaurant menu")
    print("enter 5 : for restaurant bill")
    print("enter 6 : for laundry bill")
    print("enter 7 : for complete bill")
    print("enter 8 : for exit:")
    
    try:
        userinput = int(input("enter your choice"))
        if userinput == 1:
            registercust()
        elif userinput == 2:
            roomtypeview()
        elif userinput == 3:
            roomrent()
        elif userinput == 4:
            restaurantmenuview()
        elif userinput == 5:
            orderitem()
        elif userinput == 6:
            laundrybill()
        elif userinput == 7:
            viewbill()
        elif userinput == 8:
            quit()
        else:
            print("Enter a valid number")

        
    except ValueError:
        exit("\n  that's not a number")

Menuset()
def runagain():
    runagn = input("\n want to run again y/n:")
    while runagn.lower() == 'y':
        if platform.system() == "windows":
            print(os.system('cls'))
        else:
            print(os.system('cls'))
        Menuset()
        runagn = input("\n want to run again y/n:")
runagain()
