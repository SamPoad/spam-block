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
        cursor.execute("SELECT id FROM known_fraud_item ORDER BY last_update DESC LIMIT 1")
        print("Table: known_fraud_item already exists") 
        # in which case we should drop the table contents
        # cursor.execute("DROP TABLE known_fraud_item")
    except sqlite3.OperationalError:
        cursor.execute(
            """"
            CREATE TABLE known_fraud_item (
                id, 
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


# CALL THE FUNCTION 
prepare_table()