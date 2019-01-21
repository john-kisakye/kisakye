"""Write a function called
 greatest_number that accepts a list of integers 
 seperated by a comma and 
 then returns the greatest number"""
 # Python program to find the largest number among the three input numbers
 
def greatest_number(num1, num2, num3):

	if((num1 > num2) and (num1 > num3)):
		return num1
		
	elif(num2 > num1) and (num2 > num3):
		return num2
	
	else:
		return num3

print("The greatest number of all the three is: " + str(greatest_number(5,10,6)))
