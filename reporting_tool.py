#!/usr/bin/env python2.7
# Code for generating reports.
# This is a project in the Full Stack Web Developer nanodegree program

import psycopg2

DBNAME = 'news'


def mp_articles():
    """Print out articles sorted by access."""

    query = '''
              SELECT title, count(*) AS num
              FROM log JOIN articles
              ON path LIKE CONCAT('/article/', slug)
              GROUP BY title ORDER BY num DESC LIMIT 3
            '''
    result = run_query(query)
    print '******Most popular articles******'
    for title, viewCount in result:
        print("\"{}\" -- {} views").format(title, viewCount)
    print '*********************************'


def mp_authors():
    """Print out authors sorted by popularity."""

    query = '''
              SELECT name, num FROM authors
              JOIN (SELECT author, count(*) AS num
              FROM log JOIN articles
              ON path LIKE CONCAT('/article/', slug)
              GROUP BY author ORDER BY num DESC) AS subq
              ON authors.id = subq.author
            '''
    result = run_query(query)
    print '******Most popular authors******'
    for author, viewCount in result:
        print("{} -- {} views").format(author, viewCount)
    print '********************************'


def error_report():
    """Print out dates with too much errors."""

    query = '''
              SELECT * from
              (SELECT a.date, ((a.num*100.0)::numeric/b.num) AS percentage
              FROM (SELECT cast(time as date) AS date, count(*) AS num
              FROM log WHERE status!='200 OK' GROUP BY date) AS a
              JOIN (SELECT cast(time as date) AS date, count(*) AS num
              FROM log GROUP BY date) AS b
              ON a.date=b.date ORDER BY percentage DESC) AS c
              WHERE percentage>1
            '''
    result = run_query(query)
    print '**********Saddest days**********'
    for date, error in result:
        print("{0:%B %d, %Y} -- {1:.2f}% errors".format(date, error))
    print '********************************'


def run_query(query):
    """Excute a query and return the result"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            db.close()


if __name__ == '__main__':
    mp_articles()
    mp_authors()
    error_report()
