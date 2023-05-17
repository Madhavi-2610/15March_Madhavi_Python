def findnum(no):
    max=len(no[0])
    temp=no[0]
    for i in no:
        if (len(i)>max):
            max=len(i)
            temp=i
    print(temp,max)

no=["hello","hii","python"]
findnum(no)