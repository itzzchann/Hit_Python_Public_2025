n=int(input("nhap so phan tu: "))
a=[(input(f"nhap phan tu thu {i+1}: ")) for i in range(n)]
b=tuple(a)
count=sum(1 for x in b if x.isdigit())
print("so phan tu la so:", count)