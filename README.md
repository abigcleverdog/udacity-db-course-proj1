### Version 2.0
# Overview
This program is to meet the requirement of the 'Full Stack Web Developer' nanodegree. The program report_tool.py is a Python code writen in Python 2.7.13. The program analyzes a sql database ('news') and generates three (3) meaningful statistic reports of the user behavior.
1. Most popular articles.
Example:
```
******Most popular articles******
"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views
*********************************
```
2. Most popular authors.
Example:
```
******Most popular authors******
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
********************************
```
3. On which days did more than 1% of requests lead to errors.
```
Example:
**********Saddest days**********
July 17, 2016 -- 2.26% errors
********************************
```
# How to use
The program is developed in a virtual machine of Ubuntu 16.04.2 environment. It has not been tested in other systems.
To use the program, you need to:
 - set up a command line terminal to run Python
 - install psycopg2 
```sh
$ pip install psycopg2
```
or
```sh
$ sudo pip install psycopg2
```
 - create a emplty database called 'news'
 - set up the 'news' database with the newsdata.sql file which can be downloaded from: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```sh
$ psql -d news -f newsdata.sql
```
 - run the report_tool.py in the command line
```sh
$ python report_tool.py
```
# License
MIT


### Version 1.0
If the 'news' database is set, run the report_tool.py in a command line will return three reports that meet the 

requirement of the project.
No view was created. Each report was generated with one query and sub-querie(s).

***********************
Special thanks to my Udacity reviewer (I wish I know your name but I could not find it) for the spontaneous and detailed feedback.