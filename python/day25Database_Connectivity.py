# #Database Connectivity
# #Check Connection
# import mysql.connector
# conn = mysql.connector.connect(
#     host="localhost",
#     port="3307",
#     user="root",
#     password="1234"
# )
# if conn.is_connected():
#     print("Connected Successfylly")

# #Create Cursor
# cursor = conn.cursor()

# #Create Database
# cursor.execute(
#     "CREATE DATABASE IF NOT EXISTS company"
# )

# #Use Database
# cursor.execute("USE company")

# #Create Table
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS employees(
#                id INT AUTO_INCREMENT PRIMARY KEY,
#                name VARCHAR(100),
#                salary FLOAT)
#                """)

# #Insert Data
# info =[
#     ("Arun",50000),
#     ("Varun",55000)
# ]
# cursor.executemany(
#     "INSERT INTO employees(name,salary) VALUES(%s,%s)",
#     info
# )
# conn.commit()

# #Retrieve Data
# cursor.execute(
#     "SELECT*FROM employees"
# )
# row = cursor.fetchall()
# for data in row:
#     print(data)

# #Update Data
# cursor.execute(
#     "UPDATE employees SET salary=%s WHERE id=%s",
#     (60000,3)
# )
# conn.commit()

# #Delete Data
# cursor.execute(
#     "DELETE FROM employees WHERE id IN (2,4,5,6)",   
# )
# conn.commit()

# #Complete MySQL Example
# import mysql.connector
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     port="3307",
#     password="1234",
#     database="company"
# )
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS employees(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(40),
#     salary FLOAT )
# """)
# data=[
#     ("varun",60000),
#     ("sri",30000)
# ]
# cursor.executemany(
#     "INSERT INTO employees(name,salary) VALUES(%s,%s)",
#     data
# )
# conn.commit()
# cursor.execute(
#     "SELECT * FROM employees"
# )
# for row in cursor.fetchall():
#     print(row)


# #SQLite Database Connectivity
# #Import sqlite3
# import sqlite3
# #Connect to Database
# conn = sqlite3.connect("student.db")
# #Create Cursor
# cursor = conn.cursor()
# #Create Table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students(
#                id INTEGER PRIMARY KEY,
#                name TEXT,
#                age INTEGER
#                )""")
# #Save Changes
# conn.commit()
# #Close Connection
# conn.close()

# #Inserting Data into SQLite
# import sqlite3 
# conn = sqlite3.connect("student.db")
# cursor = conn.cursor()

# cursor.execute("INSERT INTO students(name,age) VALUES (?,?)",
# ("John",20)
# )
# conn.commit()
# conn.close()

# #Retrieving Data
# import sqlite3
# conn = sqlite3.connect("student.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM students")
# for row in cursor.fetchall():
#     print(row)
# #conn.close

# #Updating Data
# cursor.execute(
#     "UPDATE students SET age=? Where id=?",
#     (26,1)
# )
# conn.commit()

# #Deleting Data
# import sqlite3

# conn = sqlite3.connect("student.db")
# cursor = conn.cursor()
# cursor.execute(
#     "DELETE FROM students WHERE id IN (2,3,4,5,6,7,8)"
# )
# conn.commit()
# conn.close()