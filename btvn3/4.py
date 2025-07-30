name=input("nhap ho ten: ")
name.strip
name.lower()
words=name.split()
words=[word.capitalize()for word in words]
chuanhoa=' '.join(words)
print("Ho ten chuan hoa:",chuanhoa)