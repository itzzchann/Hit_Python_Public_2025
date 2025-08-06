n=int(input("nhap so phan tu: "))
tup_str=tuple((input(f"nhap phan tu thu {i+1}: ")) for i in range(n))
tup_int=tuple((int(x) for x in tup_str))
average=sum(tup_int)/n if(tup_int) else 0 
print("tuple ban dau:",tup_str)
print("tuple da chuyen doi:",tup_int)
print("trung binh cong:",average)
