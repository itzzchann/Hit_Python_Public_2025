n=int(input("nhap n: "))
a=[int(input()) for i in range(n)]
x=int(input("nhap X: "))
print(f"so lan xuat hien cua {x} trong list la:  {a.count(x)}")
if(n>=7):
      a[1:7] = [8, 5, 4, 0, 1, 3]
      print("list sau khi thay doi",a)
else:
      print("list qua ngan")
print(f"so lon nhat trong list",max(a))
print(f"so nho nhat trong list",min(a))
y=int(input("nhap y: "))
a.insert(0,y);
print("List sau khi chèn:", a)
if(a==sorted(a)):
      print("TANG")
elif(a==sorted(a,reverse=True)):
     print("GIAM")
else :
    print("NO")