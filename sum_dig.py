a=int(input("enter the number"))
s=0
p=1
while a!=0:
 m=a%10
 s=s+m
 p=p*m
 a=a//10
print("the sum of digits",s)
print("product of digits",p)
