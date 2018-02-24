#!/usr/bin/env python3
import psycopg2
import configparser


def most_popular_articles(db_con):
    db_cur = db_con.cursor()
    db_cur.execute("""
    SELECT
      articles.title as title, COUNT(*) as access_count
    FROM
      articles, log
    WHERE
      log.path = CONCAT('/article/', articles.slug)
    GROUP BY
      articles.title
    ORDER BY
      access_count DESC
    LIMIT 3
    """)
    return db_cur.fetchall()


def most_popular_authors(db_con):
    db_cur = db_con.cursor()
    db_cur.execute("""
    SELECT
      authors.name as title, COUNT(*) as article_count
    FROM
      articles, authors, log
    WHERE
      authors.id = articles.author
      AND log.path = CONCAT('/article/', articles.slug)
    GROUP BY
      authors.name
    ORDER BY
      article_count DESC
    """)
    return db_cur.fetchall()


def error_days(db_con):
    db_cur = db_con.cursor()
    db_cur.execute("""
    SELECT
      log_total.day,
      (100.0 * log_errors.requests / log_total.requests) as percent
    FROM
      (
        SELECT COUNT(*) AS requests, date(time) as day
        FROM log
        WHERE status != '200 OK'
        GROUP BY date(time)
      ) AS log_errors,
      (
        SELECT COUNT(*) AS requests, date(time) as day
        FROM log
        GROUP BY date(time)
      ) AS log_total
    WHERE
      log_total.day = log_errors.day
      AND (100.0 * log_errors.requests / log_total.requests) > 1
    """)
    return db_cur.fetchall()


config = configparser.ConfigParser()
config.read('config.ini')

db_con = psycopg2.connect(
    dbname=config["DB"]["name"],
    user=config["DB"]["user"],
    password=config["DB"]["password"],
    host=config["DB"]["host"],
    port=config["DB"]["port"]
)

print("1. What are the most popular three articles of all time?")
articles = most_popular_articles(db_con)
for article in articles:
    print(article[0] + " - " + str(article[1]) + " views")

print("")
print("2. Who are the most popular article authors of all time?")
authors = most_popular_authors(db_con)
for author in authors:
    print(author[0] + " - " + str(author[1]) + " views")

print("")
print("3. On which days did more than 1% of requests lead to errors?")
errors = error_days(db_con)
for error in errors:
    print(
        error[0].strftime('%Y-%m-%d') + " - "
        + str(round(error[1], 2)) + '% errors'
    )
