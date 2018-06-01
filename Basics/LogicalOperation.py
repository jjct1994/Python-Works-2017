
def main():

	x = 8   #list of variables
	y = 3
	z = 5

	num1 = x%z    #list of operations
	num2 = z//y
	num3 = x//y
	num4 = y+z
	num5 = x%y

	ineq1 = num1 < y     #list of inequalities 
	ineq2 = y < z
	ineq3 = num2 < y
	ineq4 = num3 > z
	ineq5 = not(x < y)
	ineq6 = not(num5 < z)
	ineq7 = x > num4

	print(str("x=8, y=3, and z=5"))
	print()
	print()
	print("(x % z < and y < z) is", ineq1 and ineq2)
	print()
	print("(z//y < y or x//y > z) is", ineq3 or ineq4)
	print()
	print("(not(x < y) and x > y+z) is", ineq5 and ineq7)
	print()
	print("(x > y < z) is", x > y < z)
	print()
	print("(not(x % y < z) is", not(num5 < z))



main()
