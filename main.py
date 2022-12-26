
# IMPORT DEPENDENCIES 
import sqlite3 
from table_preparation import prepare_table

# CREATE THE CONNECTION TO THE DATABASE 
connection = sqlite3.connect("monitor.db")

# CREATE THE CURSOR 
cursor = connection.cursor() 

print("Connected to the Monitor Database")

permanent_blocks = cursor.execute(
    "SELECT * FROM known_fraud_item WHERE expiry_date IS NULL").fetchall()
print("Showing permanently blocked email addresses")
print([record for record in permanent_blocks])

temporary_blocks = cursor.execute(
    """SELECT * FROM known_fraud_item WHERE expiry_date IS NOT NULL
    """).fetchall()
print("Showing temporarily blocked emails addresses")
print([_ for _ in temporary_blocks])

# for row in cursor.execute("SELECT * FROM known_fraud_item"): 
#    print(row)