f1=open("demo file.txt","r")
f2=open("test file.txt","w")
for line in f1:
    f2.write(line)