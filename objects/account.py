import sql_queries
from connection import cursor

class Account:
    def __init__(self, id, password):
        if id is None or id < 0:
            id = 0
        self.id = id
        self.password = password

    def display(self):
        """
        cursor.execute(sql_queries.select_employee,self.id)
        result = cursor.fetchone()
        cursor.execute(sql_queries.select_job,result[4])
        job = cursor.fetchone()
        """
        cursor.execute(sql_queries.select_employee,(self.id,))
        result = cursor.fetchone()
        cursor.execute(sql_queries.select_job,(result[4],))
        job = cursor.fetchone()
        print(f"\n\nID : {self.id}\nName : {result[1]} {result[2]}\nJob : {job[0]}\nPassword : {self.password}\n\n")
