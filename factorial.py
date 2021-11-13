#wap to find out the factoria of a number
n = int(input('enter the number '))
fact = 1
while (n>1):
    fact=fact+n
    n=n-1
print('factorial of the given no. is ',fact)
