class Course:
    def __init__(self, course_code, course_name, capacity):
        self.course_code = course_code
        self.course_name = course_name
        self.capacity = capacity
        self.enrolled_students = []

    def enroll(self, student_name):
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_name)
            print(student_name + " enrolled in " + self.course_name)
            return True
        else:
            print("Course is full")
            return False

    def show_info(self):
        print(self.course_code + " - " + self.course_name + " (" + str(len(self.enrolled_students)) + "/" + str(self.capacity) + ")")   

    def show_enrolled(self):
        print(self.course_name + " enrolled students:", self.enrolled_students) 