M=int(input("Nhập tháng: "))
Y=int(input("Nhâp Năm: "))
def Day(M,Y):
    match M:
        case 1|3|5|7|8|10|12 :
            return 31
        case 4|6|9|11:
            return 30
        case 2:
            if (Y%4==0 and Y%100!=0)or(Y%400==0):
                return 29
            else :
                return 28
        case _:
            return "tháng không hợp lệ"
print(Day(M,Y))
        
    