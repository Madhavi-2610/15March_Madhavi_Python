str1=input("Enter First String:")
str2=input("Enter Sub String:")
count=0

for i in str1:
    if i==str2:
     count +=1

print(f"substring {str2} occurs {count} times in the string")


