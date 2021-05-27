import mysql.connector

mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
mycursor = mysqldb.cursor()
# create database
mycursor.execute("create database dbpy")

#create table
mycursor.execute("create table avengers(id INT, name VARCHAR(255), age INT)")

#insert in table
try:
    mycursor.execute("insert into avengers values(1, 'tony', 48),(2, 'Het', 20),(3, 'Thor', 1500),(4, 'Captain' 101),(5, 'bruce', 49),(6, 'Natasha', 34)")
    mysqldb.commit()
    print('inserted successfully')
except:
    mysqldb.rollback()

#read
try:
    mycursor.execute("select * from avengers")
    result = mycursor.fetchall()
    for i in result:
        id = i[0]
        name = i[1]
        age = i[2]
        print(id,name,age)
except:
    print('unable to fetch data')

# update
try:
    mycursor.execute("UPDATE avengers SET name='Peter', age=18 WHERE id=1")
    mysqldb.commit()
    print('updated successfully')
except:
    mysqldb.rollback()

try:
    mycursor.execute("select * from avengers")
    result = mycursor.fetchall()
    for i in result:
        id = i[0]
        name = i[1]
        age = i[2]
        print(id,name,age)
except:
    print('unable to fetch data')

# delete
try:
    mycursor.execute("DELETE FROM student WHERE id=4")
    mysqldb.commit()
    print('deleted successfully')
except:
    mysqldb.rollback()

try:
    mycursor.execute("select * from avengers")
    result = mycursor.fetchall()
    for i in result:
        id = i[0]
        name = i[1]
        age = i[2]
        print(id,name,age)
except:
    print('unable to fetch data')

mysqldb.close()