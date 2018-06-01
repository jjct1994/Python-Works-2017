#Jossue Cervantes Torres, Stephen Owiti
#Homework 5 Question 1
#WeatherDataSQL.py


#import sql module
import sqlite3	as lite
import sys

#weather file name
WEATHER_FILE = "weather.db"

#Values
records = [(100, "Dallas", "USA", 1, 24.8, 5.9),
(101, "Dallas", "USA", 2, 28.4, 16.2),
(102, "Dallas", "USA", 3, 27.9, 1549.4),
(103, "Dallas", "USA", 4, 27.6,346.0),
(104, "London", "United Kingdom", 1, 4.2, 207.7),
(105, "London", "United Kingdom", 2, 8.3, 169.6),
(106, "London", "United Kingdom", 3, 15.7, 157.0),
(107, "London", "United Kingdom", 4, 10.4, 213.5),
(108, "Cairo", "Egypt", 1, 13.6, 16.5),
(109, "Cairo", "Egypt", 2, 20.7, 6.5),
(110, "Cairo", "Egypt", 3, 27.7, 0.1),
(111, "Cairo", "Egypt", 4, 22.2, 4.5)]

#Insert Query in SQL
INSERT_RECORDS = '''INSERT INTO weather (ID,
City, Country, Season, Temperature, Rainfall)
VALUES (?,?,?,?,?,?) '''

def main():

	try:
	#connection

		connect = lite.connect(WEATHER_FILE)

		#cursor object

		crsr = connect.cursor()

		#command to create new table
		crsr.execute('''CREATE TABLE weather (
			ID INT NOT NULL,
			City TEXT(20) NOT NULL,
			Country TEXT(20) NOT NULL,
			Season INT NOT NULL,
			Temperature REAL,
			Rainfall REAL,
			PRIMARY KEY (ID));''')

		
		#cursor query inserts all values to the table

		crsr.executemany(INSERT_RECORDS, records)

	
	#exeption error
	except lite.Error as Err:
		print(Err)
		#commit new table 
	else:
		print("Data Succesfully added to weather.db")
		connect.commit()

		#close connection
	finally:

		connect.close()
main()
