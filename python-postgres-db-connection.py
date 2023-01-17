import psycopg2

#connect to the db
connection = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="dvdrental",
    user="postgres",
    password= "ILoveMedellin20!")

#cursor
cur = connection.cursor()
connection.set_session(autocommit=True)

cur.execute("SELECT first_name from actor")

rows = cur.fetchall()

for r in rows:
    print (f" First Name: {r[0]}")



#close the connection
connection.close()