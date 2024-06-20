import sqlite3

# include tabulate for better visually pleasing table output
from tabulate import tabulate

class Database:
    def __init__(self, db_name):
        # create the database connection
        self.connection = sqlite3.connect(db_name)

        # cursor will allow us to navigate around the database
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # create the table
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS rikishi(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ranking TEXT NOT NULL,
                    name TEXT NOT NULL,                    
                    origin TEXT NOT NULL,
                    stable TEXT NOT NULL)
        ''')

    def clear_table(self):
        # uncomment if you want to clear the values from table
        #self.cursor.execute('DELETE FROM rikishi')

        # uncomment if you want to delete the table entirely
        #self.cursor.execute('DROP TABLE rikishi')

        self.connection.commit()

    def insert_rikishi(self, ranking, name, origin, stable):
        self.cursor.execute('INSERT INTO rikishi (ranking, name, origin, stable) VALUES (?, ?, ?, ?)', (ranking, name, origin, stable))

        self.connection.commit()    

    # test if values inserted correctly
    def print(self):
        self.cursor.execute('SELECT * FROM rikishi')

        rows = self.cursor.fetchall()

        # grab the column names
        column_names = [description[0] for description in self.cursor.description]

        print(tabulate(rows, headers=column_names, tablefmt="grid"))

    def close(self):
        self.connection.close()

db = Database('sumo_data.db')

#db.clear_table()

db.print()
db.close()