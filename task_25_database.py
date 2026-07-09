import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# ---------------- Add Student ----------------
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (name, age, course)
    )

    conn.commit()
    print("Student Added Successfully!\n")


# ---------------- View Students ----------------
def view_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent List")
    print("--------------------------")

    for student in students:
        print(student)

    print()


# ---------------- Update Student ----------------
def update_student():

    id = int(input("Enter Student ID: "))
    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_course = input("Enter New Course: ")

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (new_name, new_age, new_course, id)
    )

    conn.commit()

    print("Student Updated Successfully!\n")


# ---------------- Delete Student ----------------
def delete_student():

    id = int(input("Enter Student ID to Delete: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()

    print("Student Deleted Successfully!\n")


# ---------------- Search Student ----------------
def search_student():

    choice = input("Search by (1) ID or (2) Name: ")

    if choice == "1":

        id = int(input("Enter ID: "))

        cursor.execute(
            "SELECT * FROM students WHERE id=?",
            (id,)
        )

    elif choice == "2":

        name = input("Enter Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE name=?",
            (name,)
        )

    student = cursor.fetchall()

    print("\nSearch Result")

    for s in student:
        print(s)

    print()


# ---------------- Main Menu ----------------
while True:

    print("====== Student Database ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        search_student()

    elif choice == "6":
        conn.close()
        print("Database Closed.")
        break

    else:
        print("Invalid Choice\n")