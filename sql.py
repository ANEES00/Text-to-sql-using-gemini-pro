import sqlite3

#connect to sqlite
connection=sqlite3.connect("Student.db")

cursor = connection.cursor()

# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ram', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Rahul', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Raj', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('ROhan', 'Data Science', 'C')''') 

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()