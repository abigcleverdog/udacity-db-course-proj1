#!/usr/bin/env python2.7
# Code for generating reports.
# This is a project in the Full Stack Web Developer nanodegree program

import psycopg2

DBNAME = 'news'


def mp_articles():
    """Print out articles sorted by access."""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
              SELECT title, count(*) AS num
              FROM log JOIN articles
              ON path LIKE CONCAT('/article/', slug)
              GROUP BY title ORDER BY num DESC LIMIT 15
            '''
    c.execute(query)
    result = c.fetchall()
    print '******Most popular articles******'
    for i in result:
        print '"' + i[0] + '"' + '--' + str(i[1]) + ' views'
    print '*********************************'
    db.close()


def mp_authors():
    """Print out authors sorted by popularity."""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
              SELECT name, num FROM authors
              JOIN (SELECT author, count(*) AS num
              FROM log JOIN articles
              ON path LIKE CONCAT('/article/', slug)
              GROUP BY author ORDER BY num DESC) AS subq
              ON authors.id = subq.author
            '''
    c.execute(query)
    result = c.fetchall()
    print '******Most popular authors******'
    for i in result:
        print i[0] + '--' + str(i[1]) + ' views'
    print '********************************'
    db.close()


def error_report():
    """Print out dates with too much errors."""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
              SELECT * from
              (SELECT to_char(a.date, 'Month DD, YYYY') AS date,
              (round(((a.num*100.0)::numeric/b.num),2)) AS percentage
              FROM (SELECT cast(time as date) AS date, count(*) AS num
              FROM log WHERE status!='200 OK' GROUP BY date) AS a
              JOIN (SELECT cast(time as date) AS date, count(*) AS num
              FROM log GROUP BY date) AS b
              ON a.date=b.date ORDER BY percentage DESC) AS c
              WHERE percentage>1
            '''
    c.execute(query)
    result = c.fetchall()
    print '**********Saddest days**********'
    for i in result:
        print i[0] + ' -- ' + str(i[1]) + '% errors'
    print '********************************'
    db.close()


mp_articles()
mp_authors()
error_report()
