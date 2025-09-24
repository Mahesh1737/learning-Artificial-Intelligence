import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mahesh@8329904289',
    database='Company_db'
)


curr = conn.cursor()
curr.execute("CREATE DATABASE IF NOT EXISTS Company_db")
print("Database created successfully")

curr.execute("""
CREATE TABLE IF NOT EXISTS employees (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
role VARCHAR(50),
salary FLOAT)
""")
print("Table Employee created successfully")

sql = "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)"


values = [
("Komal", "Data Analyst", 34000),
("Payal", "Project Manager", 50000),
('Arjun Patil', 'Software Developer', 75000),
('Priya Sharma', 'Project Manager', 110000),
('Rohan Desai', 'Data Analyst', 85000)
]

print("Row inserted successfully")
curr.executemany(sql, values)
conn.commit()

print(curr.rowcount, "row inserted")

# curr.execute("select * from employees")

# for row in curr.fetchall():
#     print(row)

#Filter record

# curr.execute("select * from employees where salary>40000")
# for row in curr.fetchall():
#     print(row)

#update record

# curr.execute("UPDATE employees SET role = 'senior analyst' WHERE role = 'Data Analyst' LIMIT 1")
# conn.commit()

# print("Data updated successfully")

# Delete an employee by ID
# employee_id = 2
# curr.execute("delete from employees where id=%s", (employee_id,))
# conn.commit()
# print("Employee deleted successfully")

# order by 3 highest paid employee
# curr.execute("SELECT * FROM employees ORDER BY salary DESC LIMIT 3")
# for row in curr.fetchall():
#     print(row)



# curr.execute("""
# CREATE TABLE IF NOT EXISTS departments (
#     dept_id INT AUTO_INCREMENT PRIMARY KEY,
#     dept_name VARCHAR(50),
#     emp_id INT,
#     FOREIGN KEY (emp_id) REFERENCES employees(id)
# )
# """)
# print("Table departments created successfully")


# department_data = [
#     ('HR', 1),
#     ('IT', 6),
#     ('Finance', 3),
#     ('IT', 4),
#     ('HR', 5)
# ]

# q = "INSERT INTO departments (dept_name, emp_id) VALUES (%s, %s)"

# curr.executemany(q, department_data)
# conn.commit()
# print("Department data inserted successfully")



#Join Query
# curr.execute("""
# SELECT employees.name, departments.dept_name
# FROM employees
# JOIN departments ON employees.id = departments.emp_id
# """)
# for row in curr.fetchall():
#     print(f"Employee: {row[0]}, Department: {row[1]}")



# #search
# search_name = "Kom" 
# curr.execute("SELECT * FROM employees WHERE name LIKE %s", (f"%{search_name}%",))
# print("Search results:")
# for row in curr.fetchall():
#     print(row)


#Drop Table
# curr.execute("DROP TABLE IF EXISTS departments")
# print("Departments table dropped if it existed.")


# Transaction
# try:
#     conn.start_transaction()
#     emp_id = 1  # Change to the employee ID you want to update
#     curr.execute("UPDATE employees SET salary = salary * 1.10 WHERE id = %s", (emp_id,))
#     # Simulate error for testing rollback (uncomment to test)
#     # raise Exception("Simulated error")
#     conn.commit()
#     print("Salary updated successfully")
# except Exception as e:
#     conn.rollback()
#     print("Transaction failed and rolled back:", e)


curr.close()
conn.close()
