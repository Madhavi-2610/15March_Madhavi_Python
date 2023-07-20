n = int(input("\n\t\tEnter Lines To Read : "))
f = open("demo file.txt","r")
for i in range(n):
	print(f.readline())