import sqlite3

conn= sqlite3.connect("C:\\Users\\rakes\\records-of-failure\\marks.db")
cur=conn.cursor()
cur.execute("create table if not exists marks (name char(20) primary key, subject char(30), marks int)")
conn.commit()
cur.close()