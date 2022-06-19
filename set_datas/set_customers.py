from faker import Faker
from connection import connection,cursor


def set_customers():
    faker = Faker()

    firstnames = [faker.first_name() for i in range(1000)]
    lastnames = [faker.last_name() for i in range(1000)]
    phones = [faker.phone_number() for i in range(1000)]
    addresses = [faker.address() for i in range(1000)]


    all = []
    for i in range(1000):
        all.append([firstnames[i],lastnames[i],phones[i],addresses[i]])

    sql = "INSERT INTO Customers(first_name,last_name,phone,address) VALUES(?,?,?,?)"
    cursor.executemany(sql,all)
    """
    For mssql:
    cursor.commit()
    """
    connection.commit()
