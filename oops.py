# A simple example class 
class Test: 
	
	# A sample method 
	def fun(self,x,y): 
		print(x,'+',y,'=',x+y) 

# Driver code
x,y=int(input()),int(input())
obj = Test() 
obj.fun(x,y) 
