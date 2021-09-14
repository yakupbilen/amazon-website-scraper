from connection import cursor
import sql_queries
class Employee:
    def __init__(self,id ,first_name, last_name, hire_date, job, salary, phone, address):
        if id is None or id < 0:
            id = 0
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.job = job
        self.salary = salary
        self.phone = phone
        self.address = address

    def display(self):
        print(f"\n\nID : {self.id}\nName : {self.first_name} {self.last_name}\nHire date : {self.hire_date}\nJob :{self.job}\n"
              f"Salary : {self.salary}\nPhone : {self.phone}\nAddress : {self.address}\n\n")