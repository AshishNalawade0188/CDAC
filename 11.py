s = 'India Is My Country'
CU = 0
CL = 0

for i in s:
    if i.isupper():
        CU+=1
    else:
        CL+=1
print("Uppercase Count :",CU)
print("Lowercase Count :",CL)


        