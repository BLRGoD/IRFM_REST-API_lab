import sqlite3
from sqlite3 import Error
import pandas as pd

# Создание БД
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
    res = dict((y[0], y[1:]) for y in rows) #вывод в виде id: values
    return res
    conn.close()


#INSERT записи в таблицу
def insert_into_table(database_name, table_name, line_df):
    conn = sqlite3.connect(database_name)
    line_df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

#Удаление записи из таблицы
def delete_from_table(database_name, table_name, line_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table_name} WHERE id = {line_id}')
    conn.commit()
    conn.close()

#Задание F
def houses_sold_sum(database_name,table_name,year,month):
  dct_month = {1 : "01", 2 : "02", 3 : "03", 4 : "04", 5 : "05", 6 : "06", 7 : "07", 8 : "08", 9 : "09", 10 : "10", 11 : "11", 12 : "12"}
  df = pd.DataFrame(select_from_table(database_name,table_name)).T
  new_column_names = {0: 'date', 1: 'price', 2: 'yr_built', 3: 'yr_renovated', 4: 'sqft_living', 5: 'condition', 6: 'real_year'}
  df = df.rename(columns=new_column_names)
  df['year'] = df['date'].str.slice(0, 4)
  df['month'] = df['date'].str.slice(4, 6)
  filt_df = df[(df['year'] == str(year)) & (df['month'] == dct_month[month])]
  return filt_df["price"].sum()

#UPDATE table
def update_table(database_name, table_name, line_id, column, new_value):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {table_name} SET {column} = {new_value} where id = {line_id}')
    conn.commit()
    conn.close()

create_connection('house_data.db')












