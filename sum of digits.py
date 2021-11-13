x = int(input('enter a no.'))
sum=0
n=None
while x>0:
     n=x%10
     sum=sum+n
     x=x//10
print('the sum of digits =',sum)
