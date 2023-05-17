def add(word):
    if len(word)< 3:
        res=word
    elif word[-3:] == "ing":
        res=word + "ly"
    else:
        res=word + "ing" 
    print(res)

word=input("enter any string")
add(word)