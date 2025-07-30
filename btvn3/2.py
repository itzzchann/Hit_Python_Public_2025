k=int(input("nhap k: "))
ds=[int(input(f"nhap k[{i}] = "))for i in range(k)]
n=int(input("nhap so hang cua ma tran: "))
m=int(input("nhap so cot cua ma tran: "))
if n*m>k:
    print("NO")
else:
    mt=[]
    idx=0
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(ds[idx])
            idx+=1
        mt.append(row)
print("Ma tran duoc tao ra: ")
for row in mt :
    print(row)
