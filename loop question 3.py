#Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number.
A=int(input('Enter the no. of which youn need the multiplication TABLE:'))
B=1
multi=0
while B<11:
        multi=A*B
        print((A),('X'),(B),"=",multi)
        B+=1
        
        
