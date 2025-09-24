import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mahesh@8329904289',
    database='Company_db'
)


curr = conn.cursor()

curr.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50),
    emp_id INT,
    FOREIGN KEY (emp_id) REFERENCES employees(id)
)
""")
print("Table departments created successfully")


department_data = [
    ('HR', 1),
    ('IT', 2),
    ('Finance', 3),
    ('IT', 4),
    ('HR', 5)
]

q = "INSERT INTO departments (dept_name, emp_id) VALUES (%s, %s)"

curr.executemany(q, department_data)
conn.commit()
print("Department data inserted successfully")

# # 11. Join Query: Fetch employee names with their department names
# curr.execute("""
# SELECT employees.name, departments.dept_name
# FROM employees
# JOIN departments ON employees.id = departments.emp_id
# """)
# for row in curr.fetchall():
#     print(f"Employee: {row[0]}, Department: {row[1]}")

# # ...existing code...