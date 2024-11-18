import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="gaming"
)
mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
)""");
print("Table created successfully")

sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("Updated.email@example.com", 1)
# val2 = ("John", "john@example.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
sql = "DELETE FROM customers WHERE id = 3"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

mycursor.execute("SELECT * FROM customers WHERE id = 1")
myresult = mycursor.fetchone()
print(myresult)

mycursor.execute("SELECT * FROM customers WHERE id = 2")
myresult = mycursor.fetchone()
print(myresult)

mycursor.execute("SELECT * FROM customers")


myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# sql = DELETE FROM customers WHERE id = 3    

# sql = "UPDATE customers SET email = %s WHERE id = %s"
# val = ("updated.email@example.com", 1)
# mycursor.execute(sql, val)
# mydb.commit() 
# print(mycursor.rowcount, "record(s) updated.")   


# sql = "INSERT INTO enoch (name, email) VALUES (%s, %s)"
# val = ("John", "john@example.com")
# mycursor.execute(sql, val)
# mydb.commit()  # Commit the changes
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM enoch")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)
mycursor.close()
mydb.close()
print("connection closed")
