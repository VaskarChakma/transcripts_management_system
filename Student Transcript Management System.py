import csv

def welcome_menu():
    print("""
****************************************
1. CREATE NEW
2. SHOW ALL
3. QUERY
0. SAVE AND QUIT
****************************************
    """)

def create_new(students):
    while True:
        print("Create a new student. Please input the following details:")
        major = input("Major: ")
        student_id = input("ID: ")
        name = input("Name: ")
        gender = input("Gender: ")
        subject = input("Subject: ")
        score = int(input("Score: "))

        # Add the new student to the list
        students.append({
            "Major": major,
            "ID": student_id,
            "Name": name,
            "Gender": gender,
            "Subject": subject,
            "Score": score
        })
        print("Student info successfully created.")

        # Ask if the user wants to create another student
        continue_choice = input("Would you like to continue to create a new one? Y/N: ").strip().upper()
        if continue_choice != 'Y':
            break

def show_all(students):
    if not students:
        print("No students to display.")
        return

    print("Please choose the mode for display:")
    print("1. Sort by ID\n2. Sort by Score")
    choice = int(input("Your choice: "))

    if choice == 1:
        students.sort(key=lambda x: x["ID"])
    elif choice == 2:
        students.sort(key=lambda x: x["Score"], reverse=True)

    print(f"{'Major':<10}{'ID':<10}{'Name':<15}{'Gender':<10}{'Subject':<15}{'Score':<10}")
    for student in students:
        print(f"{student['Major']:<10}{student['ID']:<10}{student['Name']:<15}{student['Gender']:<10}{student['Subject']:<15}{student['Score']:<10}")

def query_module(students):
    name_to_query = input("Please input the student name for query: ")
    filtered_students = [s for s in students if s['Name'] == name_to_query]

    if not filtered_students:
        print("Student not found.")
        return

    student = filtered_students[0]
    print(f"Major: {student['Major']}\nID: {student['ID']}\nName: {student['Name']}\nGender: {student['Gender']}\nSubject: {student['Subject']}\nScore: {student['Score']}")

    print("Please choose the operation on this student:")
    print("1. Modify\n2. Delete\n0. Back to the menu")
    choice = int(input("Your choice: "))

    if choice == 1:
        modify_student(student)
    elif choice == 2:
        students.remove(student)
        print("Student record deleted successfully.")

def modify_student(student):
    print("Modify the info of the student. Press Enter to keep the current value.")

    student['Major'] = input(f"Major ({student['Major']}): ") or student['Major']
    student['Subject'] = input(f"Subject ({student['Subject']}): ") or student['Subject']
    score_input = input(f"Score ({student['Score']}): ")
    student['Score'] = int(score_input) if score_input else student['Score']

    print("Modification is successful!")

def save_and_quit(students):
    with open('student.csv', 'w', newline='') as csvfile:
        fieldnames = ['Major', 'ID', 'Name', 'Gender', 'Subject', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    print("File successfully saved. Welcome next use!")

def main():
    students = []

    while True:
        welcome_menu()
        choice = int(input("Please choose a module: "))

        if choice == 1:
            create_new(students)
        elif choice == 2:
            show_all(students)
        elif choice == 3:
            query_module(students)
        elif choice == 0:
            save_and_quit(students)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
