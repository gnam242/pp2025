import math
import numpy as np
import curses

class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.gpa = 0

    def show(self):
        print(f"{self.sid} - {self.name} - {self.dob} - GPA: {self.gpa}")


class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit

    def show(self):
        print(f"{self.cid} - {self.name} ({self.credit} credits)")


class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark


class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"--- Student {i+1} ---")
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            print(f"--- Course {i+1} ---")
            cid = input("Course ID: ")
            name = input("Course name: ")
            credit = int(input("Credits: "))
            self.courses.append(Course(cid, name, credit))

    def input_marks(self):
        print("Available courses:")
        for c in self.courses:
            c.show()

        cid = input("Enter course ID to input marks: ")

        print("Enter marks for each student:")
        for s in self.students:
            raw = float(input(f"Mark for {s.name}: "))
            m = math.floor(raw * 10) / 10
            self.marks.append(Mark(cid, s.sid, m))

    def list_students(self):
        print("\n=== Students ===")
        for s in self.students:
            s.show()

    def list_courses(self):
        print("\n=== Courses ===")
        for c in self.courses:
            c.show()

    def show_marks(self):
        cid = input("Enter course ID: ")
        print(f"\nMarks for course {cid}:")
        for mk in self.marks:
            if mk.course_id == cid:
                for s in self.students:
                    if s.sid == mk.student_id:
                        print(f"{s.name}: {mk.mark}")

    def calc_gpa(self):
        for s in self.students:
            credits = []
            marks = []
            for mk in self.marks:
                if mk.student_id == s.sid:
                    for c in self.courses:
                        if c.cid == mk.course_id:
                            credits.append(c.credit)
                            marks.append(mk.mark)
            if len(credits) > 0:
                a = np.array(credits)
                b = np.array(marks)
                s.gpa = round(np.sum(a * b) / np.sum(a), 2)

    def sort_gpa(self):
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def curses_ui(self):
        def draw(stdscr):
            stdscr.clear()
            stdscr.addstr(1, 2, "=== Student Mark Manager ===")
            stdscr.addstr(3, 4, "Simple UI using curses")
            stdscr.addstr(5, 4, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        curses.wrapper(draw)


def main():
    manager = StudentMarkManager()
    manager.curses_ui()

    manager.input_students()
    manager.input_courses()

    while True:
        print("\n--- MENU ---")
        print("1. Input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show marks")
        print("5. Calculate GPA")
        print("6. Sort by GPA")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            manager.input_marks()
        elif choice == "2":
            manager.list_students()
        elif choice == "3":
            manager.list_courses()
        elif choice == "4":
            manager.show_marks()
        elif choice == "5":
            manager.calc_gpa()
            print("GPA calculated.")
        elif choice == "6":
            manager.sort_gpa()
            print("Sorted by GPA.")
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
