from multiprocessing.connection import Connection
import sqlite3
from sqlite3 import Error

from django.db import connection
#'db_file' is the name of the database file residing in a folder path,instead if you pass ':memeory:' i will create a db file existing in the ram of the system
def create_database(db_file):
    """creates a sqlite3 database based on the db_file name 
    received as parameter
    :param db_file:database filename
    :return:"""
    connection=None
    try:
        connection=sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Connected to database Successfully!")
    except Error as Err:
        print(f"Error :{Err}")
    finally:
        if connection:
            connection.close()

def create_connection(db_file):
    """creates a dtabase connection object and returns it
    :param db_file:database filename
    :return:Connection Object or None"""
    connection=None 
    try:
        connection=sqlite3.connect(db_file)
        print("Connected to database Successfully!")
    except Error as Err:
        print(f"Error :{Err}")

    return connection


def create_table(connection,create_sql):
    """creates a table in the database object passed as the argument by 
    executing the sql using cursor object
    :param connection:database connection object
    :param create_sql:create table sql query
    :return:"""
    try:
        cursor=connection.cursor()
        cursor.execute(create_sql)
        print('Created Table Successfully!')
    except Error as Err:
        print(f'Error: {Err}')


def insert_query(connection,sql,values):
    """creates a cursor object and executes the sql passed to it 
    :param connection:db connection object
    :param sql:sql query
    :param values:values passed to sql query """
    try:
        cursor=connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        print("Values Inserted to the table Successfully!")
    except Error as Err:
        print(f"Error: {Err}")

    
def update_query(connection,sql,values):
    """creates a cursor object & executes the update query
    :param connection:db connection object
    :param sql:update sql query
    :param values:values to be passed to update query"""

    try:
        cursor=connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        print("updated rows")
    except Error as e:
        print("Error: {e}")


def select_query(connection,sql,values=None):
    """creates a cursor object & executes the select query
    :param connection:db connection object
    :param sql:update sql query
    :param values:values to be passed to update query"""
    try:
        cursor=connection.cursor()
        if values:
            cursor.execute(sql,values)
        else:
            cursor.execute(sql)

        rows=cursor.fetchall()
        print("selected rows")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error:{e}")

def delete_query(connection,sql,values):
    """creates a cursor object & executes the delete query
:param connection:db connection object
:param sql:update sql query
:param values:values to be passed to update query"""
    try:
        cursor=connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        print("deleted successfully!")
    except Error as e:
        print('Error: {e}')


def insert_many_query(connection,sql,values):
    """creates a cursor object & executes the update query
:param connection:db connection object
:param sql:update sql query
:param values:values to be passed to update query"""
    try:
        cursor=connection.cursor()
        cursor.executemany(sql,values)
        connection.commit()
        print("inserted rows successfully!")
    except Error as e:
        print(f'Error : {e}')



def main():
    database=r"E:\__WORKSPACE__\Advanced Python/Advanced-Python-Topics\Databases With Python/sqlite_test.db"
    createsql="""
    CREATE TABLE IF NOT EXISTS student(
        id integer PRIMARY KEY,
        name text NOT NULL,
        age integer
    )
    """
    connection=create_connection(database)

    if connection:
        create_table(connection,createsql)
    else:
        print("failed to connect to database")

    insert_sql='''
    INSERT INTO student (id,name,age)
    VALUES (?,?,?)'''

    value1=(1,"Ravi",23)
    value2=(2,"Raju",27)

    insert_query(connection,insert_sql,value1)
    insert_query(connection,insert_sql,value2)

    update_sql="""
    UPDATE student 
    SET name=?,
    age=?
    WHERE id=?"""

    update_value=("Kiran",33,1)
    update_query(connection,update_sql,update_value)

    select_sql="""select * from student"""
    select_query(connection,select_sql)

    delete_sql="DELETE FROM student where id=?"
    delete_value=(2,)
    delete_query(connection,delete_sql,delete_value)

    insert_sql="""
    INSERT INTO student (id,name,age)
    VALUES(?,?,?)"""

    multiple_values=[(3,"Krish",34),
    (4,"Karan",43),
    (5,"Ramya",23),
    (6,"Arys",44)]

    insert_many_query(connection,insert_sql,multiple_values)

if __name__=='__main__':
    main()
   