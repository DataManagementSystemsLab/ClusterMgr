import mysql.connector
import datetime
#fix identation
# Establish connections to the source and target databases


# Connect to the source and destination d
# atabases

# Create cursors
def delete_data(destination_db, destination_table):
    destination_cursor = destination_db.cursor()
    delete_query = f"set sql_safe_updates =0;delete from {destination_table};"
    destination_cursor.execute(delete_query)
    destination_db.commit()
    destination_cursor.close()

def move_data(source_db, destination_db, source_table, destination_table, delete=False):
    if delete:
        delete_data(destination_db, destination_table)
    source_cursor = source_db.cursor()
    destination_cursor = destination_db.cursor()
    source_cursor.execute(f"SHOW COLUMNS FROM {source_table}")
    columns_table1 = [column[0] for column in source_cursor.fetchall()]

    # Get a list of columns for table2
    destination_cursor.execute(f"SHOW COLUMNS FROM {destination_table}")
    columns_table2 = [column[0] for column in destination_cursor.fetchall()]

    # Find common columns
    common_columns = set(columns_table1).intersection(columns_table2)
    common_columns = list(common_columns)
    cmdsql=f"SELECT " +",".join(common_columns) +f" FROM {source_table}"
    # Query to select the tuples from the source table
    print(cmdsql)
    source_cursor.execute(cmdsql)
    source_data = source_cursor.fetchall()

    # Insert the retrieved data into the destination table
    for row in source_data:
        # You can process and manipulate the data as needed here
        # For example, you can deserialize JSON or parse text data from the source table
        # and then insert it into the destination table
        # For this example, we are directly inserting the data
        quoted_row = ['"' + str(value) + '"' if isinstance(value, str) or isinstance(value,datetime.datetime) else value for value in row]
        quoted_row1 = ["Null" if value is None else value for value in quoted_row]
        id=quoted_row1[common_columns.index('id')]
        delete_query = f"delete from {destination_table} where id={id};"
        destination_cursor.execute(delete_query)
        insert_query = f"INSERT INTO {destination_table} ( "+",".join(common_columns)+") VALUES (" + ",".join(map(str,quoted_row1)) + ");"
        print(insert_query)
        destination_cursor.execute(insert_query)
    source_cursor.close()
    destination_cursor.close()    
    destination_db.commit()

# Define the table names in the source and destination
#source_table = 'users'
#destination_table = 'users'    
    
#move_data(source_cursor, destination_cursor, source_table, destination_table)
#destination_db.commit()

# Close the database connections
#source_db.close()
#destination_db.close()

