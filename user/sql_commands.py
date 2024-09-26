# user/sql_commands.py

def create_users_table(conn):
    """
    Create the users table if it doesn't exist.
    The function takes a database connection object and executes the SQL command.
    """
    cursor = conn.cursor()
    
    # SQL command to create the users table
    sql_command = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    '''
    
    # Execute the command
    cursor.execute(sql_command)
    add_columns_to_users_table(conn)
    
    # Commit the changes to the database
    conn.commit()


def add_columns_to_users_table(conn):
    """
    Adds 'is_admin' and 'is_active' columns to the 'users' table if they don't already exist.
    """
    cursor = conn.cursor()

    # Check if 'is_admin' column exists
    cursor.execute("PRAGMA table_info(users);")
    columns = [column[1] for column in cursor.fetchall()]

    if 'is_admin' not in columns:
        # Add 'is_admin' column
        cursor.execute("ALTER TABLE users ADD COLUMN is_admin BOOLEAN NOT NULL DEFAULT 0")
        print("Added 'is_admin' column to 'users' table.")

    if 'is_active' not in columns:
        # Add 'is_active' column
        cursor.execute("ALTER TABLE users ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT 1")
        print("Added 'is_active' column to 'users' table.")
