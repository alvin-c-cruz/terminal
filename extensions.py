import sqlite3

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Initialize the database and create the 'users' table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

# Method to close the application
def close_app(app):
    app.quit()  # Close the application
