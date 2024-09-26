import sqlite3
from pathlib import Path
from user.sql_commands import create_users_table


# Function to connect to the database
def get_db_connection():
    db_path = Path.cwd() / 'instance' / 'data.db'
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Initialize the database and create the 'users' table if it doesn't exist
def init_db():
    conn = get_db_connection()
    
    # Create users table using the function in sql_commands.py
    create_users_table(conn)
    
    conn.close()

# Method to close the application
def close_app(app):
    app.quit()  # Close the application
