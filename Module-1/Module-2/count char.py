char = input("enter any String:")
char_freq={}
for i in char:
    char_freq[i]=char_freq.get(i,0)+1
for i, j in char_freq.items():
    print(i,":",j)