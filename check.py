
a= tuple(map(int, input().split()))
b={}
for x in a:
    if x in b: 
        b[x]+=1
    else:
        b[x]=1
for key,value in b.items():
    if value%5==0 and value%10!=0:
        print(key,end=" ")

