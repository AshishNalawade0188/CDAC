S = input("Enter a string :")
cv = 0
cc= 0
for i in S:
    if i in ("aeiouAEIOU"):
        cv+=1
    else:
        cc+=1
print("the count of consonents :",cc)