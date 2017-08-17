#!/usr/bin/env python3

#Log Analysis Project
#Udacity Full-Stack Nanodegree

#importing Postgresql library
import psycopg2

#import datetime.date module for 
#problem 3
from datetime import date



''' In this one I have created VIEWS within the news database
to answer the problem set

Problem 3:
On which days did more than 1% of requests lead to errors?
CREATE VIEW BRQSTS AS 
SELECT time::timestamp::date, 
COUNT (*) as wrqsts 
FROM log
WHERE status LIKE '404 NOT FOUND'
GROUP BY time::timestamp::date 
ORDER BY time ASC;

CREATE VIEW timerqsts AS 
SELECT time::timestamp::date, 
COUNT (*) as requests 
FROM log 
GROUP BY time::timestamp::date;

CREATE VIEW error_view AS 
SELECT timerqsts.time, 
(cast(BRQSTS.wrqsts as float)/cast(timerqsts.requests as float))*100 
AS error 
FROM BRQSTS 
JOIN timerqsts on BRQSTS.time = timerqsts.time
ORDER BY error;''' 

#Global database name
DBNAME = 'news'


def execute_Query(query):
	"""execute_Query takes a string and it excutes the query
	and return the results as a list."""
	try:
		db = psycopg2.connect('dbname=' + DBNAME)
		c = db.cursor()
		c.execute(query)
		rows = c.fetchall()
		db.close()
		return rows
	except BaseException:
		Print("Unable to connect to database")


#Problem 1: What are the most popular three articles of all time?
def top_three_articles():
	query = """SELECT articles.title, COUNT (*) as views FROM 
	articles JOIN log ON articles.slug = SUBSTRING(path, 10) 
	GROUP BY path, articles.title 
	ORDER BY views  desc LIMIT 3;"""
	top_three = execute_Query(query)
	#Display header and results for Problem 1
	print('1. Top Three Articles by views')
	for i in top_three:
		print(i[0] + ' ---- ' + str(i[1]) + ' views')
	print(' ') # Display line break


#Problem 2: Who are the most popular article authors of all time?
def popular_authors():
	query = """SELECT authors.name, COUNT (*) as views 
	FROM articles INNER JOIN authors 
	ON articles.author = authors.id INNER JOIN log 
	ON articles.slug = SUBSTRING(path, 10) 
	GROUP BY name, authors.name 
	ORDER BY views desc;"""
	author_popularity = execute_Query(query)
	#display header and results for problem 2
	print('2. Most Popular article authors of all time')
	for i in author_popularity:
		print(i[0] + ' ---- ' + str(i[1]) + ' views')
	print(' ') #display line break


#Problem 3. On which days did more than 1% of requests lead to errors?
def high_error_days():
	query = """SELECT time, ROUND((error)::DECIMAL, 2)::TEXT
	FROM error_view where error > 1;"""
	high_error_results = execute_Query(query)
	#Display header and results for problem 3
	print('3. Days which more than 1% request lead to error')
	for i in high_error_results:
		print(i[0].strftime('%B %d, %Y') + ' -- ' + i[1] + '%' + ' errors')
	print(' ')#Display line break 


if __name__ == '__main__':
	print (" ")
	top_three_articles()
	popular_authors()
	high_error_days()