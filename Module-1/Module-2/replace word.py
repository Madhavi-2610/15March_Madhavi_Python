def poorraplace(str):
    not_index=str.find("not")
    poor_index=str.find("poor")
    if not_index !=-1 and poor_index !=-1 and not_index<poor_index:
        return str[:not_index]+"good"+str[poor_index+4:]
    else:
        return str
str=input("")
x=poorraplace(str)
print(x)