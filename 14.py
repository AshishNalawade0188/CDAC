str = input("Enter a string :")
ct = 0

for i in str:
    if i.isdigit():
        ct+=int(i)
        
print(ct)
