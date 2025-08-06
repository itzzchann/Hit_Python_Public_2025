arr=[1,2,3,4,5,6,7,8,9,10]
A={1,3,7,9}
B={2,4,8}
happy=0
for i in arr:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print("Số lượng số hạnh phúc:", happy)