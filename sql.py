import sqlite3
import mysql.connector

# SQLite and MySQL configuration
sqlite_db = 'final_zomato_restaurants.db'
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Vineeth04!',
    'database': 'final_zomato_restaurants'  # Ensure this database exists in MySQL
}

def migrate_sqlite_to_mysql(sqlite_db, mysql_config):
    # Connect to SQLite database
    sqlite_conn = sqlite3.connect(sqlite_db)
    sqlite_cursor = sqlite_conn.cursor()

    # Connect to MySQL database
    mysql_conn = mysql.connector.connect(**mysql_config)
    mysql_cursor = mysql_conn.cursor()

    # Table name to migrate
    table_name = 'final_restaurants'
    print(f"Processing table: {table_name}")

    # Get SQLite table schema
    sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
    columns = sqlite_cursor.fetchall()

    if not columns:
        print(f"No columns found for table {table_name}.")
        return

    # Identify the primary key column
    primary_key_column = None
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for col in columns:
        col_name = col[1]
        col_type = convert_sqlite_type_to_mysql(col[2])
        if col[5] == 1:  # 1 indicates the column is a primary key in SQLite
            primary_key_column = col_name
        create_table_query += f"`{col_name}` {col_type}, "
    
    # Finalize the CREATE TABLE query
    if primary_key_column:
        create_table_query += f"PRIMARY KEY (`{primary_key_column}`))"
    else:
        create_table_query = create_table_query.rstrip(', ') + ")"

    try:
        mysql_cursor.execute(create_table_query)
    except mysql.connector.Error as err:
        print(f"Error creating table {table_name}: {err}")
        return

    # Insert data into MySQL
    sqlite_cursor.execute(f"SELECT * FROM {table_name};")
    rows = sqlite_cursor.fetchall()
    column_names = [f"`{col[1]}`" for col in columns]

    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
    
    try:
        mysql_cursor.executemany(insert_query, rows)
        mysql_conn.commit()
    except mysql.connector.Error as err:
        print(f"Error inserting data into table {table_name}: {err}")

    # Close connections
    sqlite_conn.close()
    mysql_conn.close()
    print("Migration complete.")

def convert_sqlite_type_to_mysql(sqlite_type):
    mapping = {
        'INTEGER': 'INT',
        'TEXT': 'TEXT',
        'REAL': 'FLOAT',
        'BLOB': 'BLOB',
        'NUMERIC': 'DECIMAL'
    }
    return mapping.get(sqlite_type.upper(), 'TEXT')

if __name__ == "__main__":
    migrate_sqlite_to_mysql(sqlite_db, mysql_config)
