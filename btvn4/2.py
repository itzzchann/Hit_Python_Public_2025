A={"001","002","003","004","005","006","007","008","009","010"}
B={"0011","0012","0013","004","0015","007","0017","0018","0019","003"}
common=A.intersection(B)
if common:
    print("Sinh viên đăng ký ở cả hai bàn:", common)
else:
    print("Không có sinh viên nào đăng ký ở cả hai bàn.")
union_sv= A.union(B)
print("Danh sách sinh viên đăng ký:", union_sv)
only_A = A.difference(B)
print("Sinh viên chỉ đăng ký ở bàn A:", only_A)
