#+,-,/,*,**
#%,//
#** to the power
# 	+ (addition operator) Example: x = 2  y = 5   z = x + y 
# 	-  (Subtraction operator) Example: x = 2  y = 5    x - y = -3
# 	*  (Multiplication operator) Example: x = 2  y = 5   x * y = 10
# 	/ (Division operator) Example: x = 2  y = 5   x / y = 0.4
# 	** (Exponential operator) Example: x = 2   y = 5   x ** y = 32	
# 	% (Modulo operator - This is the remainder of division)
#  Example: x = 2  y = 5   y % x = 1
# 	// (Floor operator - Division that result into whole numbers)
# Example: x = 30  y = 7   x // y = 4
x = 30 
y = 7  
z=x // y 
print(z)
#Convert a float to an integer with an inbuilt function in Python
temp = 56.8926 
temp=round(temp)
print(temp)
# Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
temp = 56.8926 
temp=round(temp,2)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926 
temp=round(temp,3)
print(temp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 
temp = 56.8926
result = str(temp)[:2] + "." + str(temp)[2:5]
print(result)
result= float(result)
print(result)
