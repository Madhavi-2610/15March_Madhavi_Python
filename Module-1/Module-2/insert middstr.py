def insertstr(startstr,midstr):
    mid=len(startstr)
    startstr=startstr[:mid]+ midstr + startstr[mid:]
    print(startstr)
x=input("enter string one:")
y=input("enter string two:")

insertstr(x,y)