import logging
import psycopg2
from pymongo import MongoClient

def insert_into_postgres(data):
    """Insert data into PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host ="localhost",
            port=5432,
            database="mydb",
            user="myuser",
            password="mypassword"
        )
        cursor = conn.cursor() #Allows Python code to execute PostgreSQL command in a database session

        #create table 
        # .execute() sends SQL commands to the database using the cursor object.
        cursor.execute( 
            """
        CREATE TABLE IF NOT EXIST books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255)
        );
        """)
        conn.commit() # ensures that the changes (like creating a table or inserting data) are permanently saved in the database.

        for item in data:
            title = item.get("title")
            cursor.execute("INSERT INTO books (title) VALUES (%s)", (title,))
        conn.commit()

        cursor.close()
        conn.close() 
        logging.info("Data inserted into PostgreSQL successfully.")
    except Exception as e:
        logging.error("Error inserting into PostgreSQL : %s", e)

def insert_into_mongodb(data):
    """Insert data into MongoDB."""
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["mydb"]
        collection = db["books"]
        #insert many documents
        collection.insert_many(data)
        logging.info("Data inserted into MongoDB successfully.")
    except Exception as e:
        logging.error("Error inserting into MongoDB %s", e)