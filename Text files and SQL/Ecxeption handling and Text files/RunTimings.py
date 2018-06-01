#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 Question 3
#RunTimings.py

#import modules necessary for the functions
import os.path
import math

#main function
def main():

	#creating new text file
	timingsFile = open("RunTimings.txt", "w")

	timingsFile.write("Alice 3:15, 2:45, 3:30, 2:27, 3:42\n")
	timingsFile.write("Bob 2:25, 3:15, 3:20, 2:57, 2:42, 3:27\n")
	timingsFile.write("Charlie 2:45, 3:25, 3:50, 2:27, 2:52, 3:12\n")
	timingsFile.write("David 2:15, 3:35, 3:10, 2:47")

	# closing writen file
	timingsFile.close()

	#opening same file to read from
	timingsTxt = open("RunTimings.txt", "r")

	#list with strings of every line
	athletesList = timingsTxt.readlines()

	#number of lines = number of athletes
	countAthletes = len(athletesList)

	#dictionary to store athletes as keys with respective info as values
	athletesDict = {}

	#for loop to remove unessasay character, split strings and append them to dictionary
	for i in athletesList:
		blanks = str.maketrans(",:", 2*" ")
		line = i.rstrip().translate(blanks).split()
		name = line[0]
		timings = line[1:]
		secs =[int(times) for times in timings[1::2]]
		mins =[int(times)*60 for times in timings[::2]]
		

		timings = []
		index = 0

		#for loop within converts mins to seconds and adds them to seconds
		for times in secs:
			times += mins[index]
			timings.append(times)
			index += 1
	

		#adds information to dictionary to the dictionary 
		info = {name : timings}
		athletesDict.update(info)
	
	#short title
	print("\tFrom RunningTimings.txt:")
	for lines in athletesList:
		print(lines)
	timmings = []
	print()
	
	print("  Athlete      Min        Max        Avg")	
	
	#for loop prints timmings min max and average in the right order
	for name in athletesDict.keys():
			timmings = athletesDict.get(name)
			average = sum(timmings)/len(timmings)
			print(name, " "*(12-len(name)),"%s" %(min(timmings)//60),":%.02d" %(min(timmings)%60),"    ","%s:" %(max(timmings)//60),\
				":%02d" %(max(timmings)%60),"    ", int(average//60), ":%02d" %(average%60))
	
	#closing text file read
	timingsTxt.close()


#call to main
main()