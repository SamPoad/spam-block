
# IMPORT DEPENDENCIES 
import sqlite3 
from table_preparation import prepare_table

permanent_blocks = cursor.execute(
    "SELECT item FROM known_fraud_item WHERE expiry_date IS NULL"
    ).fetchall()

print(permanent_blocks)