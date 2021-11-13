m=int(input("Enter the number"))
n=int(input("Enter another number"))
dvnd=None
dvsr=None
rem=None
if m>n:
     dvnd=m
     dvsr=n
else:
     dvnd=n
     dvsr=m
rem= dvnd%dvsr
while rem!=0:
	dvnd=dvsr
	dvsr=rem
	rem=dvnd%dvsr
print("HCF is",dvsr)

