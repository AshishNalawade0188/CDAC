s = input("Enter a string :")
p = s[:2]+s[-2:]
if len(p)<2:
  print()
else:
  print(p)