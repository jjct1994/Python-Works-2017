#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 Question 5
#ExceptionHandling.py

def main():

		#Zerodivison error clause handling
		try:
			zeroDivision()
			
		except (ZeroDivisionError):
			print("Zero Division Error in zeroDivision() function")

		#value error clause handling
		try:
			valueError()

		except ValueError:
			print("Value Error in valueError() function")

		#type error  clause handling
		try:
			typeError()
		except TypeError:
			print("Type Error in typeError() function")
		
		#indexError clause handling
		try:
			indexError()
		
		except IndexError:
			print("Index Error in indexError() function")

		#random error clause handling by using exception 
		try:
			x = int(x)

		except Exception as ex:
			print("Other errors within main() function of type:", type(ex) )
		
		#final statement 
		finally:
			print("Finally: Errors found within each function without simulating errors")
	
	

#zerodivision error function
def zeroDivision():
	x = 0
	y = 3
	z = y/x
	return z


#value error function
def valueError():
	x = int("x")

	
#type error function
def typeError():
	y = '2' + 1
	return y


def indexError():

	lists = []
	a = lists[3]
	return a
	

main()