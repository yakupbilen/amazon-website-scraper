import sql_queries
from connection import cursor
from objects.employee import Employee
from objects.product import Product
from objects.customer import Customer
from objects.account import Account
from objects.sales_detail import SalesDetail
from PyQt5 import QtWidgets,QtGui

class Select:
    @staticmethod
    def getImage(imageBool):
        imagelabel = QtWidgets.QLabel()
        imagelabel.setText("")
        imagelabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageBool,"jpg")
        pixmap.scaled(100,100)
        imagelabel.setPixmap(pixmap)
        return imagelabel

    @staticmethod
    def convert_employee(tuple,job):
        return Employee(tuple[0],tuple[1],tuple[2],tuple[3],job,tuple[5],tuple[6],tuple[7])

    @staticmethod
    def select_employee(id):
        """
        cursor.execute(sql_queries.select_employee,id)
        """
        cursor.execute(sql_queries.select_employee,(id,))
        employee = cursor.fetchone()
        if employee:
            """
            cursor.execute(sql_queries.select_job,employee[4])
            """
            cursor.execute(sql_queries.select_job,(employee[4],))
            job = cursor.fetchone()
            return Select.convert_employee(employee,job[0])
        else:
            return ""

    @staticmethod
    def select_employees():
        cursor.execute(sql_queries.select_employees)
        employees = cursor.fetchall()
        list_employees = []
        for employee in employees:
            """
            cursor.execute(sql_queries.select_job,employee[4])
            """
            cursor.execute(sql_queries.select_job,(employee[4],))
            job = cursor.fetchone()
            list_employees.append(Select.convert_employee(employee,job[0]))
        return list_employees

    @staticmethod
    def convert_product(tuple):
        return Product(tuple[0],tuple[2],tuple[3],tuple[4],tuple[5],tuple[6],tuple[1])

    @staticmethod
    def select_product(id):
        """
        cursor.execute(sql_queries.select_product,id)
        """
        cursor.execute(sql_queries.select_product,(id,))
        product = cursor.fetchone()
        if product:
            return Select.convert_product(product)
        else:
            return ""

    @staticmethod
    def select_products():
        cursor.execute(sql_queries.select_products)
        products = cursor.fetchall()
        list_products = []
        for product in products:
            list_products.append(Select.convert_product(product))
        return list_products

    @staticmethod
    def convert_customer(tuple):
        return Customer(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4])

    @staticmethod
    def select_customer(id):
        """
        cursor.execute(sql_queries.select_customer, id)
        """
        cursor.execute(sql_queries.select_customer, (id,))
        customer = cursor.fetchone()
        if customer:
            return Select.convert_customer(customer)
        else:
            return ""

    @staticmethod
    def select_customers():
        cursor.execute(sql_queries.select_customers)
        customers = cursor.fetchall()
        list_customers = []
        for customer in customers:
            list_customers.append(Select.convert_customer(customer))
        return list_customers

    @staticmethod
    def convert_account(tuple):
        return Account(tuple[0],tuple[1])

    @staticmethod
    def select_account(id):
        """
        cursor.execute(sql_queries.select_account, id)
        """
        cursor.execute(sql_queries.select_account, (id,))
        account = cursor.fetchone()
        if account:
            return Select.convert_account(account)
        else:
            return ""

    @staticmethod
    def select_accounts():
        cursor.execute(sql_queries.select_accounts)
        accounts = cursor.fetchall()
        list_accounts = []
        for account in accounts:
            list_accounts.append(Select.convert_account(account))
        return list_accounts

    @staticmethod
    def convert_sales_detail(tuple):
        return SalesDetail(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4])

    @staticmethod
    def select_sales_detail(sales_id):
        """
        cursor.execute(sql_queries.select_sales_detail,sales_id,product_id)
        """
        cursor.execute(sql_queries.select_sales_detail,(sales_id,))
        results = cursor.fetchall()
        if results:
            list_details = []
            for detail in results:
                list_details.append(Select.convert_sales_detail(detail))
            return list_details
        else:
            return ""

    @staticmethod
    def select_category(id):
        cursor.execute(sql_queries.select_categories_id,(id,))
        return cursor.fetchone()[0]

    @staticmethod
    def select_subcategory(category,subcategory):
        cursor.execute(sql_queries.select_sub_categories, (category,subcategory))
        return cursor.fetchone()[0]


