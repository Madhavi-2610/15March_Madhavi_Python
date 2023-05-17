def newstring(str):
    if len(str)<2:
        newstr=""
    else:
        newstr=str[:2]+str[-2:]
    print(newstr)
x=input("enter string")
newstring(x)
