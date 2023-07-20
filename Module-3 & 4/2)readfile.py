fileread = open("demo file.txt", "r")
print(fileread.read())

for i in fileread:
    print(i)

if fileread.readable():
    print("Yes...")
else:
    print("Error!")