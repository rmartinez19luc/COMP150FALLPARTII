import sqlite3

def create_users_table():
    conn = sqlite3.connect('game_data.db')  # Ensure this matches your app's database name
    cursor = conn.cursor()

    # Create the `users` table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Users table created successfully!")

if __name__ == "__main__":
    create_users_table()
