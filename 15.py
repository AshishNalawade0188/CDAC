str = input("Enter a string :")
alpha = 0

for i in str:
    if i.isalpha():
        alpha+=1
        
print(alpha)
