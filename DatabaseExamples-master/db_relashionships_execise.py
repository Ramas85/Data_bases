# Table = "Customer"
# Fields = [first_name, last_name, amount_spent]
#
# Table = "Product"
# Fields = [name, price, description]

# Many to many
# Table = "Orders"

from database import DatabaseContextManager


# TABLES
def create_table_shopcustomers():
    query = """CREATE TABLE IF NOT EXISTS SHOPCUSTOMERS(
    shopcustomer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    amount_spent INTEGER)    
    """
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


def create_table_products():
    query = """CREATE TABLE IF NOT EXISTS PRODUCTS(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,    
    price INTEGER, 
    description TEXT)   
    """
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


# REFERENCES taikosi i Customers table ir joje i customer_id
def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS ORDERS(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,            
            shopcustomer_id INTEGER,
            product_id INTEGER,                        
            FOREIGN KEY (shopcustomer_id) REFERENCES SHOPCUSTOMERS (shopcustomer_id),
            FOREIGN KEY (product_id) REFERENCES PRODUCTS (product_id)
            )"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


def drop_table_shopcustomers():
    query = """DROP TABLE SHOPCUSTOMERS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


def drop_table_products():
    query = """DROP TABLE PRODUCTS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


def drop_table_orders():
    query = """DROP TABLE ORDERS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)


# drop_table_shopcustomers()
# drop_table_products()
# drop_table_orders()


# *******************************Shop Customer CRUD**************************************


# Create function
def create_customer(first_name: str, last_name: str, amount_spent: int):
    query = f"""INSERT INTO SHOPCUSTOMERS(first_name, last_name, amount_spent) VALUES(?,?,?)"""
    parameters = [first_name, last_name, amount_spent]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Read function
def get_customers():
    query = """SELECT * FROM SHOPCUSTOMERS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function
def update_shop_customer(first_name: str, last_name: str, new_amount_spent: int):
    query = """UPDATE CUSTOMER
                SET AMOUNT_SPENT = ?,
                WHERE first_name = ?, last_name =? """
    parameters = [new_amount_spent, first_name, last_name]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Delete function
# cia istrinam darbuotoja pagal id
def delete_customer(shopcustomer_id: int):
    query = """DELETE FROM SHOPCUSTOMERS
                WHERE id = ?"""
    parameters = [shopcustomer_id]
    with DatabaseContextManager("db_relashionships_execise.py") as db:
        db.execute(query, parameters)


# *******************************Products CRUD**************************************


# Create function
def create_product(product_name: str, price: int, description: str):
    query = """INSERT INTO PRODUCTS(product_name, price, description) VALUES(?,?,?)"""
    parameters = [product_name, price, description]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Read function
def get_products():
    query = """SELECT * FROM PRODUCTS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function
def update_product_price(product_name: str, new_price: int, new_description: str):
    query = """UPDATE PRODUCTS
                SET price = ? , description = ?,
                WHERE product_name = ?"""
    parameters = [product_name, new_price, new_description]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Delete function
#  istrina produkta pagal id is produkto lenteles
def delete_product(product_id: int):
    query = """DELETE FROM PRODUCTS
                WHERE product_id = ?"""
    parameters = [product_id]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


create_table_shopcustomers()
create_table_products()
create_customer("Ramas", "Nesvarbu", 100)
create_customer("Giedre", "Nesvarbu", 200)
create_customer("Lukne", "Nesvarbu", 300)
create_table_orders()

create_product("Verzliaraktis", 15, "skirtas atsukti verzlems")
create_product("Plaktukas", 15, "skirtas kalti")
create_product("Tusinukas", 15, "skirtas rasyti")
create_product("Trintukas", 15, "skirtas trinti")
create_product("Piestukas", 15, "skirtas piesti")


# *******************************Orders CRUD**************************************

# Create function
def create_orders(shopcustomer_id: int, product_id: int):
    query = f"""INSERT INTO ORDERS(shopcustomer_id,product_id) VALUES(?,?)"""
    parameters = [shopcustomer_id, product_id]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Read function
def get_orders():
    query = """SELECT * FROM ORDERS"""
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function
def update_orders(new_order_id: int, shop_customer_id: int, product_id: int):
    query = """UPDATE ORDERS
                    SET order_id = ?,
                    WHERE shopcustomer_id = ?, product_id = ? """
    parameters = [new_order_id, shop_customer_id, product_id]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Delete function
def delete_orders(order_id: int):
    query = """DELETE FROM ORDERS
                            WHERE id = ?"""
    parameters = [order_id]
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query, parameters)


# Read function
def get_customers_products_info():
    query = """SELECT * FROM ORDERS
                JOIN SHOPCUSTOMERS ON SHOPCUSTOMERS.shopcustomer_id = ORDERS.shopcustomer_id
                JOIN PRODUCTS      ON PRODUCTS.product_id = ORDERS.product_id
                    """
    with DatabaseContextManager("db_relashionships_execise") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


create_orders(1, 9)
create_orders(2, 5)
create_orders(2, 1)
create_orders(2, 3)
get_customers_products_info()

# drop_table_SHOPCUSTOMERS()
# drop_table_PRODUCTS()
# drop_table_ORDERS()
# create_table_customers()
# create_table_products()

# create_customer("Ramas", "Mon", 100)
# create_customer("Giedre", "Mon", 200)
#


# create_table_customers()
# create_table_orders()
# create_orders(1, 2)
# get_customers_products_info()
# get_products()


# get_products()
# get_orders()
