#Jossue Cervantes Torres, Stephen Owiti
#Homework 5 Question 2
#WeatherData.py

#import SQL module

import sqlite3 as lite
import sys
#variable for file name
WEATHER_FILE = "weather.db"



def main():

	try:
		#connection to database
		connect = lite.connect(WEATHER_FILE)

	#connection error

	except lite.error as err:
		print('Could not connect to database')

	else:
		#cursos object 

		crsr = connect.cursor()

		#A)  All records for the city of london
		
		crsr.execute('SELECT * FROM weather WHERE City = "London"')
		resultA = crsr.fetchall()
		displayResult(resultA)

		#B) All the summer records
		crsr.execute("SELECT * FROM weather WHERE Season = 2")
		resultB = crsr.fetchall()
		displayResult(resultB)

		#C) city, country, and season for average temps less than 20
		crsr.execute('SELECT City,Country,Season FROM weather WHERE Temperature < 20')
		resultC = crsr.fetchall()
		displayResult(resultC)

		#D) city, country and season for average temp > 20, and rainfall < 10
		crsr.execute('SELECT City,Country,Season FROM weather WHERE Temperature > 20 and Rainfall < 10')
		resultD = crsr.fetchall()
		displayResult(resultD)

		#E)Maximum total rainfall
		crsr.execute("SELECT max(Rainfall) FROM weather")
		resultE = crsr.fetchall()
		print()
		print("Max rainfall from table is")
		displayResult(resultE)

		#F) city,Season, Rainfall, in decending order of rainfall
		crsr.execute("SELECT City,Season,Rainfall FROM weather ORDER BY Rainfall DESC")
		resultF = crsr.fetchall()
		displayResult(resultF)

		#G)Total Rainfall for cairo, egypt
		crsr.execute("SELECT SUM(Rainfall) AS AnnualRain FROM weather WHERE City = 'Cairo'")
		resultG = crsr.fetchall()
		print()
		print("Total rainfall in Cairo")
		displayResult(resultG)

		#H) City Name, country and total Yearly rainfall
		crsr.execute("SELECT City,Country,SUM(Rainfall) AS AnnualRain FROM weather GROUP BY City")
		resultH = crsr.fetchall()
		displayResult(resultH)
	

	#end connection to database
	finally:
		connect.close()


#function that print results
def displayResult(results):

	print()
	for record in results:
		for i in range(len(record)):
			print("%s" %record[i],end = '   ')
		print()

#call to main
main()




