#Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another
a=int(input('enter the first number'))
b=int(input('enter the second no.'))
rex=0
if a>b:
        rex = b**a
        print(rex)
        
elif b>a:
        rex = a**b
        print(rex)
else:
        print('your input is invalid')
        
