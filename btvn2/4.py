n=int(input("nhap xu: "))
new=n//28
vo=new
sumn=new
while vo>=3:
    doi=vo//3
    sumn+=doi
    vo=vo%3+doi
print("so chai mua duoc",sumn)
