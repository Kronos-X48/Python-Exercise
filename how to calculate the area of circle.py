# wap to teach a student how to calculate the area of a circle
import turtle
r = float(input('here we have radius of the circle ='))

print('as we know that the area of a circle is equal to (r^2)*22/7')

#formula to calculate the area = (r^2)*22/7
area=0
area= r*r*3.14

print('as we put radius of circle into the formula , there comes an output this output is the area of the desired circle')
print('area of the given circle is approximately around ',area)

turtle.Screen()
wn=turtle.Screen()
wn.title('area of circle')
tr=turtle.Turtle()
for i in range(2000):
    tr.fd(50)
    tr.rt(10)
