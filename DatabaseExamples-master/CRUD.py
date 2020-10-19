from database import DatabaseContextManager


def create_table_custumers():
    query = """CREATE TABLE IF NOT EXISTS Custumers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)



def create_custumer(first_name: str, last_name: str, age: int):
    query = f"""INSERT INTO Custumers(first_name, last_name, age) VALUES(?,?,?)"""
    # Question marks are used in initial query to have placeholders for upcoming parameters.
    # (This is used to protect ourselves from SQL Injection attacks)
    parameters = [first_name, last_name, age]
    # Parameters are used to pass values that were given when calling the function.
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
    # We can pass sql and parameters to execute method which will set our values by order from parameters array or touple


def get_custumer():
    query = """SELECT * FROM Custumers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_custumer(first_name: str, new_age: int):
    query = """UPDATE Custumers
                SET age = ?
                WHERE first_name = ?"""
    parameters = [new_age, first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_custumer():
    query = """SELECT * FROM Custumers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def delete_custumer(id: int):
    query = """DELETE FROM Custumers
                    WHERE id = ?"""
    parameters = [id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        print("------------------------------------------------------")


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS companies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        employee_count INTEGER
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_company(company_name: str, employee_count: int):
    query = f"""INSERT INTO Company(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM Company"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def get_customers_companies():
    query = """SELECT * FROM Custumers
                JOIN Companies
                    ON Custumer.company_id = Companies.company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)

# create_table_custumers()

# create_custumer("Linas", "Linelis", 25)
# create_custumer("Jonas", "Jonelis", 35)
# create_custumer("Giedre", "Giedraityte", 29)

# get_custumer()
# update_custumer("Jonas", 37)
# delete_custumer(3)

# get_custumer()
# get_custumer()

#create_table_company()
# create_company("IBM", 100)
# create_company("Maxima", 200)
# create_company("Senukai", 300)
create_company("IBMjujuju", 100)
create_company("IBMblabla", 100)
create_table_companies()
get_companies()
get_customers_companies()
