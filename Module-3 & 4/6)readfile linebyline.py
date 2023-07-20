f=open("demo file.txt","r")
line=f.readlines()
print(line)
newlines=[i.strip() for i in line ]
print(newlines)