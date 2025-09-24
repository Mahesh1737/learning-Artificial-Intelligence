import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='mahesh@8329904289', database='scope')
curr=conn.cursor()
print("connection done successfully")
# query='create database scope'
# curr.execute(query)
# print("database created successfully")

curr.execute("""
CREATE TABLE IF NOT EXISTS employees (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50),
role VARCHAR(50),
salary FLOAT)
""")

print("Table Employee screated")


sql = "INSERT INTO employees (name, city, role, salary) VALUES (%s, %s, %s, %s)"

values = [
("Komal", "Pune", "Data Analyst", 34000),
("Payal", "Pune", "Project Manager", 50000),
('Arjun Patil', 'Nashik', 'Software Developer', 75000),
('Priya Sharma', 'Mumbai', 'Project Manager', 110000),
('Rohan Desai', 'Pune', 'Data Analyst', 85000)
]

print("Values inserted successfully")


curr.executemany(sql,values)
conn.commit()

print(curr.rowcount, "row inserted")


curr.execute("select * from employees")

for row in curr.fetchall():
    print(row)


