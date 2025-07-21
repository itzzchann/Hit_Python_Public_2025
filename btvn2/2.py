def ketoan(luong):
    if luong>=15000000:
        thue=luong*0.30
    elif luong>=7000000:
        thue=luong*0.20
    elif luong>=0:
        thue=luong*0.10
    else :
        return "luong khong hop le"
    luongr=luong-thue
    return int(thue),int(luongr)
luong=int(input("nhap luong: "))  
thue,thunhap=ketoan(luong)  
print("Thue: ",thue," thu nhap: ",thunhap)

    