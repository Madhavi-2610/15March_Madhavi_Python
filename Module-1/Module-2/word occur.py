n=input("enter any string")
words=n.lower().split()
wordcount={}

for i in words:
    if i in wordcount:
        wordcount[i]+=1
    else:
        wordcount[i]=1

for i ,j, in wordcount.items():
    print(f"word {i} occurs in the sentence  {j}")