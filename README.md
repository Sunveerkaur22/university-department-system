# University Department Management System

A command-line Python application for managing students, courses, and
enrollments within a university department. Built for the B100 Introduction
to Computer Programming with Python module at Gisma University of Applied
Sciences.

---

## Project Purpose

This system was designed to help a university department:
- Keep track of registered students and the courses they take
- Manage course capacity and enrollment
- Record and update student grades per course
- Persist all data between sessions using CSV files

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sunveerkaur22/university-department-system.git
   cd university-department-system
   ```

2. **Requirements** — Python 3.8 or higher. No external libraries needed
   (only built-in Python modules are used).

3. **Run the application**
   ```bash
   python main.py
   ```

---

## Example Usage

```
--- Gisma Department System ---
1. Add student
2. Add course
3. Enroll student in course
4. Assign grade
5. List students
6. List courses
7. List enrollments
8. Save data
9. Load data
10. Exit
Choose: 1
Student ID: S001
Name: John Roy
John Roy added to Computer Science

Choose: 2
Course code: CS101
Course name: Computer Science
Capacity: 30
Computer Science added to Computer Science

Choose: 3
Student ID: S001
Course code: CS101
John Roy enrolled in Computer Science

Choose: 4
Student ID: S001
Course code: CS101
Grade: 85
Grade 85 assigned to S001 in CS101
```

---

## Key Features

| Feature | Description |
|---|---|
| Student management | Add students, view their grade records |
| Course management | Add courses with a defined enrollment capacity |
| Enrollment | Enroll a student in a course (capacity-checked) |
| Grading | Assign or update a grade for an enrolled student |
| Reporting | List all students, courses, or enrollments |
| Data persistence | Save and load all data to/from CSV files |
| Error handling | Gracefully handles invalid numeric input (e.g. grade, capacity) |

---

## Project File Structure

```
university_system/
├── main.py                  # Entry point and menu-driven CLI
├── README.md
├── students.csv              # Auto-generated on save
├── courses.csv                # Auto-generated on save
├── enrollments.csv            # Auto-generated on save
└── modules/
    ├── __init__.py
    ├── student.py            # Student class
    ├── course.py             # Course class
    ├── enrollment.py         # Enrollment class
    └── department.py         # Department class (core controller)
```

---

## How It Works

- **`Student`** stores a student's ID, name, and a dictionary of grades per course.
- **`Course`** stores a course code, name, capacity, and list of enrolled students.
- **`Enrollment`** links a student to a course with an optional grade.
- **`Department`** is the controller — it owns all students, courses, and
  enrollments, and coordinates actions between them (e.g. checking capacity
  before enrolling, finding the right enrollment to grade).

Data is saved to three separate CSV files (`students.csv`, `courses.csv`,
`enrollments.csv`) and reloaded automatically when you choose the "Load data"
option.

---

## Module: B100 Introduction to Computer Programming with Python
**Institution:** Gisma University of Applied Sciences
**Author:** Sunveer Kaur
