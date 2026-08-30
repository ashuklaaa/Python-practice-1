a=input("Choose the current unit of temp (C/F)")
if a=="C":
    t=float(input("Enter temperature: "))
    t=(t*1.8)+32
    print("Temperature in F is",t)
else:
    t=float(input("Enter temperature: "))
    t=(t-32)/1.8
    print("Temperature in C is",t)
    