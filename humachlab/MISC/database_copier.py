import sqlite3

# Connect to the source and target SQLite databases
src_path = '../../emran/staticfiles/database/emran2.sqlite3'
dest_path = '../../emran/staticfiles/database/emran.sqlite3'

exclude_tables = ['admin', 'auth_user', 'django_migrations', 'sqlite_sequence']  # Add any tables you want to exclude

source_db = sqlite3.connect(src_path)
target_db = sqlite3.connect(dest_path)

# Create cursors to interact with both databases
source_cursor = source_db.cursor()
target_cursor = target_db.cursor()

# Function to get the list of tables in the database
def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

# Function to get the column names from a table
def get_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]  # Column names are in the second element of the tuple
    return columns

# Function to get column names and their types from a table
def get_columns_and_types(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns_info = cursor.fetchall()
    columns = [(col[1], col[2]) for col in columns_info]  # (column_name, column_type)
    return columns


def get_values_with_proper_type_conversion(column_type, value):
    column_type = column_type.upper()
    print(column_type, value)
    return_value = value
    # Handle different column types appropriately
    # if column_type in ['TEXT', 'VARCHAR']:
    if any(substring in column_type for substring in ['TEXT', 'VARCHAR']):
        if value is not None:
            value = value.replace("'", "''")
        return_value = f"'{str(value)}'" if value is not None else 'NULL'
    elif column_type == 'INTEGER':
        return_value = int(value) if value is not None else 'NULL'
    elif column_type == 'REAL':
        return_value = float(value) if value is not None else 'NULL'
    elif column_type == 'BLOB':
        return_value = value if value is not None else 'NULL'  # Handle binary data (BLOB)
    elif column_type == 'DATE':
        return_value = f"'{str(value)}'" if value is not None else 'NULL'
    elif value is None:
        return_value = 'NULL' if value is not None else 'NULL'

    print('ret-- ', return_value)
    return return_value

# Get the list of tables in the source database
tables_in_source = get_tables(source_cursor)

# Loop through each table and copy it if it's not in the exclude list
for table in tables_in_source:
    if table not in exclude_tables:
        print('='*50)
        # Get columns for both source and target tables
        source_columns = get_columns(source_cursor, table)
        target_columns = get_columns(target_cursor, table)

        print(table, source_columns, target_columns)

        # Determine columns that need to be added to the target table
        missing_columns = set(source_columns) - set(target_columns)
        extra_columns = set(target_columns) - set(source_columns)

        print('---->', table, missing_columns, extra_columns)

        # # If there are missing columns, add them to the target table
        # for column in missing_columns:
        #     source_cursor.execute(f"PRAGMA table_info({table})")
        #     column_definition = next(col for col in source_cursor.fetchall() if col[1] == column)
        #     column_type = column_definition[2]  # Get the column type
        #     target_cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {column_type}")
        #
        # Select all rows from the source table
        source_cursor.execute(f"SELECT * FROM {table}")
        rows = source_cursor.fetchall()
        print(' ###>>> ', len(rows))
        source_columns_and_types = get_columns_and_types(source_cursor, table)
        target_columns_and_types = get_columns_and_types(target_cursor, table)

        # Insert data into the target table, ensuring NOT NULL columns are handled
        for i, row in enumerate(rows):
            print(i, ' >>> ', row)
            source_dict = dict(zip(source_columns, row))
            print(source_dict)
            print(source_columns, source_columns_and_types)
            print(target_columns)
            # replace(replace( '- Great Learning Academy - Free course\r\n- ', '\r', char(13)), '\n', char(10))
            target_values = [get_values_with_proper_type_conversion(ct, source_dict[c]) if c in source_columns else 'NULL' for c, ct in target_columns_and_types]
            # target_values = [replace(replace(v, '\r', char(13)), '\n', char(10)) if v!=None else None for v in target_columns]
            print(target_values)

            # target_values = []
            #
            # for i, (column_name, column_type) in enumerate(source_columns_and_types):
            #     value = row[i]
            #     get_values_with_proper_type_conversion(column_type, value)

            # print(', '.join(target_columns), '\n', ', '.join(map(str, target_values)))
            values = f"{', '.join(map(str, target_values))}"
            sql_query = f"INSERT INTO {table} ({', '.join(target_columns)}) VALUES ({values})"
            print(sql_query)
            target_cursor.execute(sql_query)

        # # Prepare placeholders for the insertion, ensuring it matches the number of columns in the target table
        # columns = len(rows[0]) if rows else 0
        # placeholders = ', '.join(['?'] * len(target_columns))
        #
        # # Insert data into the target table, ensuring NOT NULL columns are handled
        # for row in rows:
        #     # Check for NULL values in the NOT NULL columns and replace with a default value if necessary
        #     row_data = list(row)
        #
        #     # Assuming the column 'membership_start_date' is at index 2 (adjust as needed)
        #     membership_start_date_index = target_columns.index(
        #         'membership_start_date') if 'membership_start_date' in target_columns else -1
        #     if membership_start_date_index != -1 and row_data[membership_start_date_index] is None:
        #         row_data[
        #             membership_start_date_index] = '1970-01-01'  # Replace with a default date or handle accordingly
        #
        #     # Insert NULL for missing columns in the source data
        #     row_data = row_data + [None] * (len(target_columns) - len(row_data))
        #
        #     # Insert the data into the target table
        #     target_cursor.execute(f"INSERT INTO {table} ({', '.join(target_columns)}) VALUES ({placeholders})",
        #                           row_data)

# Commit changes to the target database
target_db.commit()

# Close connections
source_db.close()
target_db.close()
