import mysql.connector
#fix identation
# Establish connections to the source and target databases

source_db_config = {
    'host': '127.0.0.1',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
}

destination_db_config = {
    #151.181.203.21
    'host': '127.0.0.1',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster1',
}

# Connect to the source and destination d
# atabases
source_db = mysql.connector.connect(**source_db_config)
destination_db = mysql.connector.connect(**destination_db_config)
# Create cursors
source_cursor = source_db.cursor()
destination_cursor = destination_db.cursor()



def move_data(source_cursor, destination_cursor, source_table, destination_table):

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
        quoted_row = ['"' + str(value) + '"' if isinstance(value, str) else value for value in row]
        quoted_row1 = ["Null" if value is None else value for value in quoted_row]
        id=quoted_row1[common_columns.index('id')]
        insert_query = f"delete from {destination_table} where id={id}; INSERT INTO {destination_table} ( "+",".join(common_columns)+") VALUES (" + ",".join(map(str,quoted_row1)) + ");"
        print(insert_query)
        destination_cursor.execute(insert_query)

    # Commit the changes to the destination database
    
# Define the table names in the source and destination
source_table = 'users'
destination_table = 'users'    
    
move_data(source_cursor, destination_cursor, source_table, destination_table)
destination_db.commit()

# Close the database connections
source_db.close()
destination_db.close()

