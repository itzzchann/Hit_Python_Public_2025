s1=input("nhap xau 1: ")
s2=input("nhap xau 2: ")
print("dao nguoc xau 1:",s1[::-1])
print("Nhập vào 2 số nguyên a, b (1 <= a < b <= len(s2)):")
a=int(input())
b=int(input())
if 1 <= a < b <= len(s2):
    s2n=s2[:a-1]+s2[a-1:b][::-1]+s2[b:]
    print("chuoi 2 sau khi dao nguoc [a.b]:",s2n)
else:
    print("gia tri a,b khong thoa man")
s3=''.join(s1[i]for i in range(len(s1))if i%2!=0)
print("s3:",s3)
max_size=max(len(s1),len(s2))
s4=''
for i in range(max_size):
    if i<len(s1):
        s4+=s1[i]
    if i<len(s2):
        s4+=s2[i]
print("s4:",s4)