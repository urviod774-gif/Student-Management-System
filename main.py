import csv

def add_student():
    sid =input("Enter student id : ")
    with open("students.csv","r",newline="")as file :
        reader=csv.reader(file)
        next(reader)
        for row in reader :
            if row[0] == sid :
                print("Student id is already exist.")
                return
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    sclass = input("Enter Class: ")
    marks = input("Enter Marks: ")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, sclass, marks])

    print("Student added successfully!")


def view_student():

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print("\nStudent ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Class:", row[3])
            print("Marks:", row[4])
            marks = int(row[4])
            if marks>=90 :
                Grade = "A"
            elif marks>=80 :
                Grade = "B"
            elif marks>=70 :
                Grade = "C"
            elif marks>=60:
                Grade = "D"
            else :
                Grade = "F"
            print("Grade:",Grade)


def search_student():

    sid = input("Enter Student ID to search: ")
    found = False

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == sid:
                print("\nStudent ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Class:", row[3])
                print("Marks:", row[4])
                marks = int(row[4])
                if marks>=90 :
                    Grade = "A"
                elif marks>=80 :
                    Grade = "B"
                elif marks>=70 :
                    Grade = "C"
                elif marks>=60:
                    Grade = "D"
                else :
                    Grade = "F"
                print("Grade:",Grade)
                
                found = True
                break

    if not found:
        print("Student not found!")


def update_student():

    rows = []
    found = False

    sid = input("Enter Student ID to update: ")

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)

        for row in reader:
            if row[0] == sid:
                found = True
                row[1] = input("Enter New Name: ")
                row[2] = input("Enter New Age: ")
                row[3] = input("Enter New Class: ")
                row[4] = input("Enter New Marks: ")

            rows.append(row)

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student():

    rows = []
    found = False

    sid = input("Enter Student ID to delete: ")

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == sid:
                found = True
            else:
                rows.append(row)

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found!")
        
def count_student():
    with open("students.csv","r",newline="")as file :
        reader=csv.reader(file)
        next(reader)
        count = 0
        for row in reader :
            count = count + 1
        print("Total Students = ",count)
        
def topper_student():
    highest_marks=-1
    topper=None
    with open("students.csv","r",newline="")as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader :
            marks = int(row[4])
            if highest_marks<marks :
                highest_marks=marks
                topper=row
    print("\n----- Topper Student -----")
    print("\nStudent ID:", topper[0])
    print("Name:", topper[1])
    print("Age:", topper[2])
    print("Class:", topper[3])
    print("Marks:", topper[4])
    marks = int(row[4])
    if marks>=90 :
        Grade = "A"
    elif marks>=80 :
        Grade = "B"
    elif marks>=70 :
        Grade = "C"
    elif marks>=60:
        Grade = "D"
    else :
        Grade = "F"
    print("Grade:",Grade)               


while True:
    print("-"*40)
    print("\n===== Student Management System =====")
    print("-"*50)
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Topper Students")
    print("8. Exit")
    print("-"*50)

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "8":
        print("Thank You!")
    
    elif choice == "6":
        count_student()
        
    elif choice =="7":
        topper_student()
        break

    else:
        print("Invalid Choice")