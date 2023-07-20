f=open("demo file.txt",'a')
data=["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."]
f.writelines(data)
print("Is File Readable:  ",f.readable())
print("Is File Writable:  ",f.writable())
print("Lines append to the filename demo file.txt successfully!!")
f.close()