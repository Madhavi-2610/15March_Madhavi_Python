f=open("demo file.txt","r")
words=f.read().split()
max_len=len(max(words,key=len))
result=[word for word in words if len(word)==max_len]
print(result)
f.close()