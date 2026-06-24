class Student:
    def __init__(self, student_id, name):
      self.student_id = student_id
      self.name = name 
      self.grades = {}  #will store course_name -> grade
    
    def show_info(self):  
      print(self.student_id + " - " + self.name) 
    
    def add_grade(self, course_name, grade):
      self.grades[course_name] = grade
      print(self.name + " received " + str(grade) + " in " + course_name)
    
    def show_grades(self):
        print(self.name + "'s grades:", self.grades)
