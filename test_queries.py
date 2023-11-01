import sqlite3

""" create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print("Error:", e)

    return conn

def select_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error:", e)

def show_db(c):
    query = """SELECT name FROM sqlite_master WHERE type = 'table'"""
    select_query(c, query)

    print("--- test to see if population worked ---")

    query = "SELECT * FROM department"
    print('\n'+query)
    select_query(c, query)

    query = "SELECT * FROM instructor"
    print('\n'+query)
    select_query(c, query)

    query = "SELECT * FROM student"
    print('\n'+query)
    select_query(c, query)

    query = "SELECT * FROM class"
    print('\n'+query)
    select_query(c, query)

    query = "SELECT * FROM enrollment"
    print('\n'+query)
    select_query(c, query)

    query = "SELECT * FROM dropped"
    print('\n'+query)
    select_query(c, query)

def show_users_db(c):
    query = """SELECT name FROM sqlite_master WHERE type = 'table'"""
    select_query(c, query)

    query = "SELECT * FROM users LIMIT 10"
    print('\n'+query)
    select_query(c, query)



def start():
    database = "database.db"
    conn = create_connection(database)
    users_database = "users.db"
    users_conn = create_connection(users_database)

    show_db(conn)
    conn.close()
    show_users_db(users_conn)
    users_conn.close()

if __name__ == "__main__":
    start()