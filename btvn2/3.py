n=int(input("nhap n: "))
xau=str(abs(n))
dai=len(xau)
tong =0
for ch in xau:
    tong+=int(ch)
print("so chu so:",dai,", tong chu so:",tong)