n=int(input("Enter n lines:"))
f=open('demo file.txt',"r")
for line in (f.readlines()[-n:]):
    print(line,end="")
f.close()