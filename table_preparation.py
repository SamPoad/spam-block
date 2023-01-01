# This page will house a function to create an SQL database and a known_fraud_item table with some example emails 

# IMPORT DEPENDENCIES 
import sqlite3 

# DEFINE THE FUNCTION 
def prepare_table():
    # CREATE THE CONNECTION AND CURSOR 
    connection = sqlite3.connect("monitor.db")
    cursor = connection.cursor() 

    # CREATE THE TABLE IF IT DOES NOT EXIST 
    try: 
        print(cursor.execute("SELECT item FROM known_fraud_item ORDER BY last_update DESC LIMIT 1").fetchone())
        print("Table: known_fraud_item already exists") 
        # in which case we should drop the table contents
        # cursor.execute("DROP TABLE known_fraud_item")
    except sqlite3.OperationalError:
        cursor.execute(
            """
            CREATE TABLE known_fraud_item (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                item, 
                item_type,
                create_date, 
                last_update, 
                expiry_date, 
                message
            )
            """
        )
        print("Table: known_fraud_item created successfully")
    
    # PUT DATA INTO THE TABLE 
    # FIRST BATCH ARE THOSE THAT ARE WITHOUT AN EXPIRY_DATE 
    cursor.execute(
        """
        INSERT INTO known_fraud_item (id, item, item_type, create_date) VALUES (
            0, 'bruce.wayne@w_enterprises.com', 'email', CURRENT_TIMESTAMP), (
            1, 'batman@batcave.com', 'email', CURRENT_TIMESTAMP), (
            2, 'ckent@dailyplanet.com', 'email', CURRENT_TIMESTAMP)
        """
    )

    # SECOND BATCH HAVE AN EXPIRATION DATE
    cursor.execute(
        """
        INSERT INTO known_fraud_item (id, item, item_type, create_date, expiry_date) VALUES (
            3, 'tony@starkindustries.com', 'email', CURRENT_TIMESTAMP, '2022-12-25 00:00:00'), (
            4, 'steverogers@whitehouse.gov', 'email', CURRENT_TIMESTAMP, '2022-12-25 00:00:00'), (
            5, 'pparker@dailybugle.com', 'email', CURRENT_TIMESTAMP, '2022-12-25 00:00:00')
        """
    )

    connection.commit()
    # VERIFY THE DATA WAS INSERTED
    # verification = cursor.execute('SELECT * FROM known_fraud_item')
    # print(f"{cursor.execute('SELECT * FROM known_fraud_item LIMIT 6')}")
    # print(verification.fetchall())
    # print(cursor.execute('SELECT * FROM known_fraud_item LIMIT 6').fetchall())

# CALL THE FUNCTION 
prepare_table()