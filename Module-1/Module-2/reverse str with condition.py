def reverse(string):
    if len(string) % 4==0:
        string=string[::-1]
    print(string)
string=input("enter string:")
reverse(string)