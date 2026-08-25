x=[6,26,5,17,24,26,12,15,5,13,24,11,12]
m=sum(x)/len(x)
print(x)
print(m)
d =[m-i for i in x]
print(d)
p=[k**2 for k in d]
s=sum(p)
print(s)
div=s/len(x)
print(div)
f=div**0.5
print(f)
