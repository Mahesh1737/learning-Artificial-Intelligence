
curr.execute("select * from employees")

for row in curr.fetchall():
    print(row)