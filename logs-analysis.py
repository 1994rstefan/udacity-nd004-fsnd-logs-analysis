#!/usr/bin/env python3
import psycopg2

db_con = psycopg2.connect(dbname="logs_analysis", user="logs_analysis", password="123qwe!\"§QWE", host="localhost", port="63322")

db_cur = db_con.cursor()

db_cur.execute("""SELECT * FROM authors""")
rows = db_cur.fetchall();
print(rows)
