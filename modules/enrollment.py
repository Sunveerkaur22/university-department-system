class Enrollment:
    def __init__(self, student_id, course_code, grade=None):
        self.student_id = student_id
        self.course_code = course_code
        self.grade = grade

    def assign_grade(self,grade):
        self.grade = grade 
        print("grade " + str(grade) + " assigned to " + self.student_id + " in " + self.course_code )
  
    def show_info(self):
        grade_display = self.grade if self.grade is not None else "not graded yet"
        print(self.student_id + " |" + self.course_code + " | grade: " + str(grade_display))
 