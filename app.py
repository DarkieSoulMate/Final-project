from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname="testnod",
            user="postgres",
            password="Asilhonbtw7",
            host="ooptest.cpk2g68mgiaf.eu-north-1.rds.amazonaws.com",
            port="5432"
        )
        print("\u2713 Connect successfuly.")
        return connection
    except Exception as e:
        print("\u2717 Connection Error:", e)
        return None

def fetch_all_data():
    conn = get_db_connection()
    if conn is None:
        print("No connection to database.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test")
        table_data = cursor.fetchall()
        print("\u2713 Data from test (DEBUG):", table_data)
        conn.close()
        return table_data
    except Exception as e:
        print("\u2717 No exist database:", e)
        return []

@app.route('/')
def index():
    table_data = fetch_all_data()
    if not table_data:
        print("\u2717 Data base table is empty.")
    return render_template('index.html', data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
