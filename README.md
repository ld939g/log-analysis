# Udacity Full-Stack Nanodegree
## Log-analysis Project

### Overview

In this project I was tasked to create a reporting tool which can print reports based on real world web-application data, with fields representing informaton that a webserver would record, such as status codes and URL paths. This reporting tool is use Python program using  `psycopg2` module to connect the database.

### Assignment

1. What are the msot popular articles of the all time?
2. Who are the most popular articles authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### PreRequisites:
* [Python3](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com)
* [Virtual Box](https://www.virtualbox.org)

#### Setup

1. Install Vagrant and VirtualBox
2. Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
4. Unzip this file after downloading it. The file inside is called newsdata.sql.
5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)


#### Launching the Virtual Machine:
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
  $ vagrant up
  ```
2. Then Log into this using command:
  
  ```
   $ vagrant ssh
   ```
3. Change directory to /vagrant and look around with ls.

### How to run

This section will describe the SQL views I created for the code to function properly and how to run the program.

#### Required SQL Views
This program uses three SQL views.

**For Problem 3:**

> `CREATE VIEW BRQSTS AS 
SELECT time::timestamp::date, 
COUNT (*) as wrqsts 
FROM log
WHERE status LIKE '404 NOT FOUND'
GROUP BY time::timestamp::date 
ORDER BY time ASC;`

> `CREATE VIEW timerqsts AS 
SELECT time::timestamp::date, 
COUNT (*) as requests 
FROM log 
GROUP BY time::timestamp::date;`

> `CREATE VIEW error_view AS 
SELECT timerqsts.time, 
(cast(BRQSTS.wrqsts as float)/cast(timerqsts.requests as float))*100 
AS error 
FROM BRQSTS 
JOIN timerqsts on BRQSTS.time = timerqsts.time
ORDER BY error;`

#### Running the queries:
1. From the vagrant directory inside the virtual machine,run logs.py using:
   ```
   $ python3 log-analysis.py
   ```
