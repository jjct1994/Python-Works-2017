#Jossue Cervantes Torres
#Quiz 3 question 5
#TmeFormat.py


#importin time module
import time
t = time.localtime(1500000000)

def main():

	
	# using time module for function to print out exact dates

	#part a
 	print("a)",time.strftime("%A, %B %d %Y", t))
 	print()

  	#part b
 	print("b)",time.strftime("%I:%M %p %Z on %m/%d/%Y", t))
 	print()

 	#part c
 	print("c)","I will meet you on",time.strftime("%a %B %d at %I:%M %p.", t))

main()