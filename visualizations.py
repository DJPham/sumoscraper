import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualization:
    def __init__(self, db_name):
        # connect to the database
        self.connection = sqlite3.connect('sumo_data.db')
        self.cursor = self.connection.cursor()

    def fetch_data(self):
        # grab all the infrom from rikishi table
        self.cursor.execute('SELECT ranking, name, origin, stable FROM rikishi')

        rows = self.cursor.fetchall()

        # make a DataFrame for the fetched data
        self.df = pd.DataFrame(rows, columns=['ranking', 'name', 'origin', 'stable'])

    # make a bar chart of the most common origins for the rikishi are
    def plot_origin_distribution(self):
        # the saved visualization will be stored in a folder called "viz" but just in case it doesn't exist    
        if not os.path.exists('viz'):
            os.makedirs('viz')

        plt.figure(figsize=(10, 6))

        # bar chart
        sns.countplot(data=self.df, x='origin', order=self.df['origin'].value_counts().index)

        plt.savefig('./viz/origin_distribution.png')

        plt.title('Origin Distribution')
        plt.xlabel('Origin')
        plt.ylabel('Count')

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    # make a bar chart of which stable has the most rikishi (in the Makuuchi division)
    def plot_stable_distribution(self):
        # the saved visualization will be stored in a folder called "viz" but just in case it doesn't exist    
        if not os.path.exists('viz'):
            os.makedirs('viz')

        plt.figure(figsize=(10, 6))

        # bar chart
        sns.countplot(data=self.df, x='stable', order=self.df['stable'].value_counts().index)

        plt.savefig('./viz/stable_distribution.png')

        plt.title('Stable Distribution')
        plt.xlabel('Stable')
        plt.ylabel('Count')

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()


    def close(self):
        self.connection.close()