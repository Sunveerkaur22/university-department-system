from modules.student import Student
from modules.course import Course
from modules.enrollment import Enrollment


class Department:
    def __init__(self, name):
        self.name = name
        self.students = {}  #will store student_id of students in the department
        self.courses = {}  #will store course_code of courses offered
        self.enrollments = []  #will store Enrollment objects

    def add_student(self, student):
        self.students[student.student_id] = student
        print(student.name + " added to " + self.name)
    
    def add_course(self, course):
        self.courses[course.course_code] = course
        print(course.course_name + " added to " + self.name)

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students :
            print("student not found") 
            return 
            
        if course_code not in self.courses:
            print("course not found") 
            return
         
        student = self.students[student_id]
        course = self.courses[course_code]

        success = course.enroll(student.name)
        if success:
           new_enrollment = Enrollment(student_id, course_code)
           self.enrollments.append(new_enrollment)
           
    def assign_grade(self, student_id, course_code, grade):    
      for e in self.enrollments:
          if e.student_id == student_id and e.course_code == course_code:
              e.assign_grade(grade)
              return 
          
      print("enrollment not found") 

    def list_students(self):
        for s in self.students.values():
            s.show_info() 

    def list_courses(self):
        for c in self.courses.values():
            c.show_info() 

    def list_enrollments(self):
        for e in self.enrollments:
            e.show_info() 

    def save_to_file(self):
        try:
            with open("students.csv", "w") as f:
                for s in self.students.values():
                    f.write(s.student_id + "," + s.name + "\n")

            with open("courses.csv", "w") as f:
                for c in self.courses.values():
                    f.write(c.course_code + "," + c.course_name + "," + str(c.capacity) + "\n")

            with open("enrollments.csv", "w") as f:
                for e in self.enrollments:
                    grade_str = str(e.grade) if e.grade is not None else ""
                    f.write(e.student_id + "," + e.course_code + "," + grade_str + "\n")

            print("All data saved successfully.")
        except IOError as err:
            print("Error saving data:", err)

    def load_from_file(self):
        try:
            with open("students.csv", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    self.add_student(Student(parts[0], parts[1]))
        except FileNotFoundError:
            print("No saved students found.")

        try:
            with open("courses.csv", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    self.add_course(Course(parts[0], parts[1], int(parts[2])))
        except FileNotFoundError:
            print("No saved courses found.")

        try:
            with open("enrollments.csv", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    grade = int(parts[2]) if len(parts) > 2 and parts[2] else None
                    self.enrollments.append(Enrollment(parts[0], parts[1], grade))
        except FileNotFoundError:
            print("No saved enrollments found.")