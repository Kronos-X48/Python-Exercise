x = int(input('Enter Your Age'))
y = input('What is your sex')
z = input('Married OR NOT Married')
if 20<=x<=40 and y==('M'):
   print('He can work Anywhere')
elif 41<=x<=60 and y==('M'):
   print("he can work in urbal areas only")
elif x>20 and y==('F'):
   print("she can work in ")
else:
    print("ERROR")
