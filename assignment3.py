students = {}

def add_student():
    name = input("Enter student name: ").lower()
    age = input("Enter age: ")
    score = input("Enter score: ")
    students[name] = {"age": age, "score": score}
    print("Student added!")

def view_students():
    if not students:
        print("No student records yet.")
    else:
        for name, info in students.items():
            print(f"{name} - Age: {info['age']}, Score: {info['score']}")

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        info = students[name]
        print(f"{name} - Age: {info['age']}, Score: {info['score']}")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
