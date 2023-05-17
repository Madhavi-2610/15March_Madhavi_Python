str1=input("enter string one:")
str2=input("enter string two:")
newstring=str2[:2]+str1[2:] + "   " + str1[:2]+str2[2:]
print("swap the two char swap is:",newstring)