from faker import Faker
from connection import cursor,connection
import random
import sql_queries,time

random.seed(time.process_time())

rolesHigh = [["Admin",7000,10000,2],["AccessAdmin",8000,12000,1]]
rolesOther = [["DataWriter",4000, 8000,3], ["DataReader", 3000,6000,4],["SalerManager",3000,4500,5], ["Saler",2500,4000,6]]
jobs = [["AccessAdmin"],["Admin"],["DataWriter"],["DataReader"],["SalerManager"],["Saler"]]
jobs_sqlite = [("AccessAdmin",),("Admin",),("DataWriter",),("DataReader",),("SalerManager",),("Saler",)]
faker = Faker()

firstnames = [faker.first_name() for i in range(50)]
lastnames = [faker.last_name() for i in range(50)]
hire_dates = [faker.date_between(start_date='-5y', end_date='today') for i in range(50)]
phones = [faker.phone_number() for i in range(50)]
addresses = [faker.address() for i in range(50)]
passwords = [faker.pystr(min_chars=8,max_chars=15) for i in range(50)]
jobs_id = []
salaries = []
for i in range(43):
    choice_ = random.choice(rolesOther)
    jobs_id.append(choice_[3])
    salaries.append(random.randint(choice_[1],choice_[2]))

for i in range(7):
    choice_ = random.choice(rolesHigh)
    jobs_id.append(choice_[3])
    salaries.append(random.randint(choice_[1],choice_[2]))


employees = []
accounts=[]
for i in range(50):
    employees.append([firstnames[i],lastnames[i],hire_dates[i].strftime("%Y-%m-%d"),jobs_id[i],salaries[i],phones[i],addresses[i]])
    accounts.append([passwords[i]])
"""
For mssql:
cursor.executemany("INSERT INTO Jobs(job) VALUES (?)",jobs)
cursor.commit()

cursor.executemany(sql_queries.insert_employee,employees)
cursor.commit()

cursor.executemany(sql_queries.insert_account,accounts)
cursor.commit()
"""
cursor.executemany("INSERT INTO Jobs(job) VALUES (?)",jobs_sqlite)
connection.commit()

cursor.executemany(sql_queries.insert_employee,employees)
connection.commit()

cursor.executemany(sql_queries.insert_account,accounts)
connection.commit()

