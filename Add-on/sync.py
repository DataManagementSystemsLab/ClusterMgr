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
    'host': '151.181.203.21',
    'user': 'owuser',
    'password': 'pass4owCluster',
    'database': 'owcluster',
}

# Connect to the source and destination d
# atabases
source_db = mysql.connector.connect(**source_db_config)
destination_db = mysql.connector.connect(**destination_db_config)

# Create cursors
source_cursor = source_db.cursor()
destination_cursor = destination_db.cursor()

# Define the table names in the source and destination
source_table = 'users'
destination_table = 'users'

# Query to select the tuples from the source table
source_cursor.execute(f"SELECT * FROM {source_table}")
source_data = source_cursor.fetchall()

# Insert the retrieved data into the destination table
for row in source_data:
    # You can process and manipulate the data as needed here
    # For example, you can deserialize JSON or parse text data from the source table
    # and then insert it into the destination table
    # For this example, we are directly inserting the data
    print (row)
    insert_query = f"INSERT INTO {destination_table} VALUES ({','.join(map(str, row))})"
    destination_cursor.execute(insert_query)

# Commit the changes to the destination database
destination_db.commit()

# Close the database connections
source_db.close()
destination_db.close()

