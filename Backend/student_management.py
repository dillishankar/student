import mysql.connector

# ✅ Connect to MySQL Database
con = mysql.connector.connect(
    host="localhost",
    user="root",       # your MySQL username
    password="dilli@2004",   # your MySQL password
    database="student_db"
)

cursor = con.cursor()

# ✅ Add Student
def add_student(name, age, grade):
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(query, values)
    con.commit()
    print("✅ Student Added Successfully!")

# ✅ View All Students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    print("-----------------------\n")

# ✅ Update Student
def update_student(student_id, new_name, new_age, new_grade):
    query = "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s"
    values = (new_name, new_age, new_grade, student_id)
    cursor.execute(query, values)
    con.commit()
    print("✅ Student Updated Successfully!")

# ✅ Delete Student
def delete_student(student_id):
    query = "DELETE FROM students WHERE id=%s"
    values = (student_id,)
    cursor.execute(query, values)
    con.commit()
    print("✅ Student Deleted Successfully!")

# ✅ Menu Driven Program
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            add_student(name, age, grade)

        elif choice == '2':
            view_students()

        elif choice == '3':
            student_id = int(input("Enter Student ID to Update: "))
            new_name = input("Enter New Name: ")
            new_age = int(input("Enter New Age: "))
            new_grade = input("Enter New Grade: ")
            update_student(student_id, new_name, new_age, new_grade)

        elif choice == '4':
            student_id = int(input("Enter Student ID to Delete: "))
            delete_student(student_id)

        elif choice == '5':
            print("Exiting Program...")
            break

        else:
            print("❌ Invalid Choice! Try Again.")

# ✅ Run the Program
menu()

# Close connection when program ends
cursor.close()
con.close()
