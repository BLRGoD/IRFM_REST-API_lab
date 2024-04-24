import sqlite3
from sqlite3 import Error
import pandas as pd

# A
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('drop table if exists HouseData')
        cursor.execute('''CREATE TABLE kc_house_data (
                    id INTEGER,
                    date TEXT,
                    price REAL,
                    yr_built INTEGER,
                    yr_renovated INTEGER,
                    sqft_living INTEGER,
                    condition INTEGER,
                    real_year INTEGER
                )''')
        data = pd.read_csv('kc_house_data.csv')
        data['real_year'] = data[['yr_built', 'yr_renovated']].max(axis=1)
        data = data[['id','date', 'price', 'yr_built', 'yr_renovated', 'sqft_living', 'condition', 'real_year']]
        data=data[data['price']>0]
        data=data[data['yr_built']>0]
        print(data.head())
        data.to_sql('kc_house_data', conn, if_exists='replace', index=False)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#SELECT из таблицы в БД
def select_from_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    res = dict((y[0], y[1:]) for y in rows)
    return res
    conn.close()

#Удаление записи из таблицы
def delete_from_table(database_name, table_name, line_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table_name} WHERE id = {line_id}')
    conn.commit()
    conn.close()


create_connection('house_data.db')












