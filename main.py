from modules.student import Student
from modules.course import Course
from modules.enrollment import Enrollment
from modules.department import Department


def show_menu():
    print("\n--- Gisma Department System ---")
    print("1. Add student")
    print("2. Add course")
    print("3. Enroll student in course")
    print("4. Assign grade")
    print("5. List students")
    print("6. List courses")
    print("7. List enrollments")
    print("8. Exit")
    print("9. Load data")
    print("10. Exit")


def main():
    dept = Department("Computer Science")

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            dept.add_student(Student(sid, name))

        elif choice == "2":
           code = input("Course code: ")
           name = input("Course name: ")
           try:
              capacity = int(input("Capacity: "))
              dept.add_course(Course(code, name, capacity))
           except ValueError:
              print("Capacity must be a number. Course not added.")

        elif choice == "3":
            sid = input("Student ID: ")
            code = input("Course code: ")
            dept.enroll_student(sid, code)

        elif choice == "4":
            sid = input("student ID: ")
            code = input("course code: ")
            try:
                grade = int(input("grade: "))
                dept.assign_grade(sid, code, grade)
            except ValueError:
                print("Grade must be a number. Grade not assigned.")

        elif choice == "5":
            dept.list_students()

        elif choice == "6": 
            dept.list_courses()

        elif choice == "7":
            dept.list_enrollments()
        
        elif choice == "8":
            dept.save_to_file()

        elif choice == "9":
            dept.load_from_file()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
    


                
main()