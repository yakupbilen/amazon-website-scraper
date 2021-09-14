select_products = "SELECT * FROM Products"
select_product = "SELECT * FROM Products WHERE id=?"
insert_product = "INSERT INTO Products(name,price,stock,category,subcategory,photo) VALUES (?,?,?,?,?,?)"
delete_product = "DELETE FROM Products WHERE id=?"
update_product = "UPDATE Products SET name=?,price=?,stock=?,category=?,subcategory=?,photo=? WHERE id=?"
update_stock_product = "UPDATE Products SET stock=? WHERE id=?"

select_customers = "SELECT * FROM Customers"
select_customer = "SELECT * FROM Customers WHERE id=?"
insert_customer = "INSERT INTO Customers(first_name,last_name,phone,address) VALUES (?,?,?,?)"
delete_customer = "DELETE FROM Customers WHERE id=?"
update_customer = "UPDATE Customers SET first_name=?,last_name=?,phone=?,address=? WHERE id=?"


select_employees = "SELECT * FROM Employee"
select_employee = "SELECT * FROM Employee WHERE id=?"
insert_employee = "INSERT INTO Employee(first_name,last_name,hire_date,job,salary,phone,address) VALUES (?,?,?,?,?,?,?)"
delete_employee = "DELETE FROM Employee WHERE id=?"
update_employee = "UPDATE Employee SET first_name=?,last_name=?,salary=?,phone=?,address=? WHERE id=?"
admin_update_emp = "UPDATE Employee SET job=? WHERE id=?"

select_accounts = "SELECT * FROM Accounts"
select_account = "SELECT * FROM Accounts WHERE emp_id=?"
insert_account = "INSERT INTO Accounts(password) VALUES (?)"
delete_account = "DELETE FROM Accounts WHERE emp_id=?"
update_account = "UPDATE Accounts SET password=? WHERE emp_id=?"
select_max_account_id = "SELECT MAX(emp_id) FROM Accounts"


select_all_sales = "SELECT * FROM Sales"
select_sales = "SELECT * FROM Sales WHERE id=?"
select_max_sales = "SELECT Max(id) From Sales"
insert_sales = "INSERT INTO Sales(emp_id,date,total_price) VALUES (?,?,?)"
update_sales = "UPDATE Sales Set total_price=? WHERE id=?"
delete_sales = "DELETE FROM Sales WHERE id=?"

select_sales_details = "SELECT * FROM Sales_Details"
select_sales_detail = "SELECT * FROM Sales_Details WHERE sales_id=?"
insert_sales_detail = "INSERT INTO Sales_Details(sales_id,product_id,amount,price) VALUES (?,?,?,?)"
update_sales_detail = "UPDATE Sales_Details SET amount=?,price=? WHERE sales_id=? AND product_id=?"
delete_sales_detail = "DELETE FROM Sales_Details WHERE sales_id=? AND product_id=?"


select_categories = "SELECT * FROM Categories"
select_categories_id = "SELECT name FROM Categories WHERE id=?"
select_category_id = "SELECT id FROM Categories WHERE name=?"
select_sub_categories = "SELECT name FROM Subcategories WHERE category_id=? AND subcategory_id=?"
select_sub_categories2 = "SELECT subcategory_id,name FROM Subcategories WHERE category_id=?"
select_sub_category_id = "SELECT subcategory_id FROM Subcategories WHERE category_id=? AND name=?"

select_jobs = "SELECT * FROM Jobs"
select_job = "SELECT job FROM Jobs WHERE id=?"
select_job_id = "Select id FROM Jobs WHERE job=?"

select_max_category = "SELECT MAX(id) FROM Categories"
select_max_subcategory = "SELECT MAX(subcategory_id) FROM Subcategories WHERE category_id=?"
