import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def insert_product(conn, product):
    sql = ''' INSERT INTO 
products(name,description,price,quantity_in_stock)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, product)
    return cur.lastrowid

def update_product(conn, product):
    sql = ''' UPDATE products
              SET name = ? ,
                  description = ? ,
                  price = ? ,
                  quantity_in_stock = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, product)

def delete_product(conn, id):
    sql = 'DELETE FROM products WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def select_all_products(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = "market.db"   # replace with the path to your database
    conn = create_connection(database)
    with conn: 
        print("Insert a new product")
        product = ('Test Product', 'This is a test product', 10.99, 100)
        product_id = insert_product(conn, product)

        print("Update the test product")
        updated_product = ('Updated Test Product', """This is an updated 
test product""", 11.99, 50, product_id)
        update_product(conn, updated_product)

        print("Display all products")
        select_all_products(conn)

        print("Delete the test product")
        delete_product(conn, product_id)

        print("Display all products")
        select_all_products(conn)

if __name__ == '__main__':
    main()

