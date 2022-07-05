

from urllib.parse import uses_params
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name,user_name,user_pasword):
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_pasword)
        print("MySql Database Connection Successful!")
    except Error as err:
        print(f"Error:{err}")
    return connection


def create_db_connection(host_name,user_name,user_passsword,db_name):
    connection=None 
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_passsword,database=db_name)
        print(f"connected to '{db_name}' database successfully!")
    except Error as err:
        print(f"Error: {err}")
    return connection

def create_database(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Successfully!")
    except Error as err:
        print(f"Error:{err}")


def execute_query(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query Successful!')
    except Error as err:
        print(f"Error :{err}")

def execute_list_query(connection,query,val):
    cursor=connection.cursor()
    try:
        cursor.executemany(query,val)
        connection.commit()
        print("Query Successful!")
    except Error as Err:
        print(f"ERROr :{Err}")


def read_query(connection,query):
    cursor=connection.cursor()
    res=None 
    try:
        cursor.execute(query)
        res=cursor.fetchall()
        return res
    except Error as err:
        print(f"Error: {err}")

connection=create_db_connection("sql6.freemysqlhosting.net","sql6493335","7XH9giFcXk","sql6493335")
print(connection)

# #create a teble

# create_student_table="""
# CREATE TABLE student(id INT PRIMARY KEY,
# name VARCHAR(40) NOT NULL,
# age INT);
# """

# execute_query(connection,create_student_table)

# #insert values

# populate_table="""
# INSERT INTO student VALUES  
# (1,"James",25),
# (2,"Ravi",22),
# (3,"Kiran",23);
# """

# execute_query(connection,populate_table)

# #read data
# read_students="""
# SELECT * FROM students;"""

# results=read_query(connection,read_query)
# print(results)

# #update data

# update_query="""
# UPDATE student
# SET name="Karan" 
# WHERE id=2;
# """
# execute_query(connection,update_query)

# #delete data

# delete_query="""
# DELETE FROM student
# WHERE id=3"""

# execute_query(connection,delete_query)

#execute a list of values

sql='''
INSERT INTO student (id,name,age) 
values (%s,%s,%s)
'''

val=[(4,"Ram",34),
(5,"Kiran",23)]

execute_list_query(connection,sql,val)



