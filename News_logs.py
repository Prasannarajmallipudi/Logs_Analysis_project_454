# !/usr/bin/env python3
# import the pyscopg2 from postgresql
import psycopg2
# we connect to the database news to the object Enadu
Enadu = psycopg2.connect(database="news")


# here define function to find popular three articles
def Most_popular_three_articles():
    print('\n  What are the most popular three articles of all time?\n')
    n = Enadu.cursor()
    query_top_articles = """SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;"""
# execute the above query
    n.execute(query_top_articles)
    articles = n.fetchall()
    for top in articles:
        print ('''    "%s" __ %d views''' % (top[0], top[1]))


# here define function to most popular authors
def Most_popular_authors():
    print('\n  Who are the most popular article authors of all time?\n')
    n = Enadu.cursor()
    query_popular_authors = """SELECT authors.name, count(log.path) as views FROM\
                 articles, log, authors\
                 WHERE log.path=('/article/'||articles.slug)\
                 AND articles.author = authors.id \
                 GROUP BY authors.name ORDER BY views desc"""
    n.execute(query_popular_authors)
    authors = n.fetchall()
    for top in authors:
        print("    %s __ %d views" % (top[0], top[1]))

''' here we define function to find On which days
    did more than 1% of requests lead to errors '''


def error_percentage():
    print('\n  On which days did more than 1% of requests lead to errors?\n')
    n = Enadu.cursor()
    query_error_calculation = """ SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC; """
    n.execute(query_error_calculation)
    errordata = n.fetchall()
    for d in errordata:
        date = d[0].strftime('    %B %d, %Y')
        errors = str(round(d[1]*100, 1)) + "%" + "  errors"
# here we need date in the format of month,day and year
        print(date + '__ '+errors)
# close the object
    Enadu.close()
# after condition is ocuur then calls the particular function and print results
if __name__ == '__main__':
    Most_popular_three_articles()
    Most_popular_authors()
    error_percentage()
