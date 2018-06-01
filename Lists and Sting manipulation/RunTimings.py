#Jossue Cervantes Torres
#Homework 2 Question 2
#RunTimings.py


def getAverage(x):
	average = sum(x)/len(x)
	return(average)

#main fuction of the program
def main ():

	#list of variables
	mins = 0
	secs = 0
	total = 0
	count = 0

	#list used for inner loop
	#will be cleared everytime outer loop is started
	listCount = []

	#list to store athletes names and info for the table
	athletesList = []
	listAverage = []
	listMin = []
	listMax = []

	#initial input
	num_of_athletes = int(input("Enter the number of athletes participating:"))

	
	for athletes in range(num_of_athletes): #first loop for each participant
		athletes_name = str(input("Enter the name of athlete %s:" %(athletes + 1))) #input for names of athletes
		athletesList.append(athletes_name) #adding atheles name to list
		while True: #inner loop to get timings 
			(mins, secs) = input("Enter %s\'s timing for 1000 meters or x,xx to quit(minutes , seconds):" %athletes_name).split(",")  #input for times, x,xx is input then loop will break
			if (mins == str("x")):
				  	#once loop is stoped average min and max are added to designated lists	
				listAverage.append(getAverage(listCount))					
				listMin.append(int(min(listCount)))
				listMax.append(int(max(listCount)))
				
				del listCount[:] #list where count of all timings is cleared for next athlete

				break

				


			else: #conversion of times to seconds and added list 
				mins = int(mins)*60
				secs = int(secs)
				listCount.append(mins + secs)
	print()
	print("  Athlete      Min        Max        Avg")			
	for i in range(num_of_athletes):  #last loop after information is gathered to print out the table with the information organized.
		print(athletesList[i], " "*(12 - len(athletesList[i])),"%s" %(int(listMin[i])//60), ":%02d" %(int(listMin[i])%60),\
			"    ", (int(listMax[i])//60),":%02d" %(int(listMax[i])%60), "    ", (int(listAverage[i])//60),":%02d" %(int(listAverage[i])%60))


		











#call to main function
main()