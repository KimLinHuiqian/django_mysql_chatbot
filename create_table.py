import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE citizens (citizen_id INT AUTO_INCREMENT, first_name VARCHAR(255), last_name VARCHAR(255), application_id INT, PRIMARY KEY (citizen_id));")
mycursor.execute("CREATE TABLE applications (application_id INT AUTO_INCREMENT, name VARCHAR(255), status VARCHAR(255), citizen_id INT, PRIMARY KEY (application_id), FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id));")
mycursor.execute("ALTER TABLE citizens ADD FOREIGN KEY (application_id) REFERENCES applications(application_id));")