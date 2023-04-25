s='a2b5c12'
num=0
for i in range (len(s)-1):
    if((s[i]>='0') and (s[i]<='9')):
      temp = s[i-1]
    while ((s[i]>='0') and (s[i]<='9')):
        n=ord(s[i])
        num=(num*10)+(n-48)
        i+=1
        for j in range(num):
            print(temp)
    num=0




