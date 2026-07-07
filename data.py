import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    """Manages MySQL database operations"""
    
    def __init__(self, host="localhost", user="root", password="", database="testdb"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("✓ Connected to database")
        except Error as e:
            print(f"✗ Error: {e}")
            return False
        return True
    
    def create_table(self):
        """Create people table if it doesn't exist"""
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            sr_no INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            city VARCHAR(100),
            income FLOAT,
            age INT,
            married VARCHAR(3)
        )
        ''')
        self.conn.commit()
        print("✓ Table created/verified")
    
    def insert_person(self, name, city, income, age, married):
        """Insert a person record"""
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO people (name, city, income, age, married)
        VALUES (%s, %s, %s, %s, %s)
        ''', (name, city, income, age, married))
        self.conn.commit()
        print(f"✓ Record inserted for {name}")
    
    def get_all_people(self):
        """Retrieve all people records"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM people")
        return cursor.fetchall()
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("✓ Connection closed")


if __name__ == "__main__":
    # Configure your MySQL credentials here
    db = DatabaseConnection(
        host="localhost",
        user="root",
        password="",  # Enter your MySQL password
        database="testdb"
    )
    
    if db.connect():
        db.create_table()
        
        # Take input
        name = input("Enter name: ")
        city = input("Enter city: ")
        income = float(input("Enter income: "))
        age = int(input("Enter age: "))
        married = input("Married? (Yes/No): ")
        
        # Insert data
        db.insert_person(name, city, income, age, married)
        
        # Display all records
        print("\n--- All People ---")
        for row in db.get_all_people():
            print(row)
        
        db.close()