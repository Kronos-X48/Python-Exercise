#Write a program that prompts the user to input a positive integer.
#It should then output a message indicating whether the number is a prime number.
x=int(input())

if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0:
        print('its not a prime no.')
else :
        print('its a prime no.')
