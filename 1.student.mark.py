students = []
courses = []
marks = {}

def input_number_students():
    n = int(input("Enter number of students: "))
    return n

def input_student_info(number):
    for i in range(number):
        print(f"\nStudent {i+1} ")
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of birth: ")
        students.append({"id": sid, "name": name, "dob": dob})

def input_number_courses():
    n = int(input("Enter number of courses: "))
    return n

def input_course_info(number):
    for i in range(number):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({"id": cid, "name": name})

def input_marks():
    print("\nAvailable courses:")
    for c in courses:
        print(f"- {c['id']}: {c['name']}")
    course_id = input("Enter course ID to input marks: ")
    if course_id not in marks:
        marks[course_id] = []
    print("\nEnter marks for each student:")
    for s in students:
        mark = float(input(f"Mark for {s['name']}: "))
        marks[course_id].append((s["id"], mark))

def list_students():
    print("\nStudents List ")
    for s in students:
        print(f"{s['id']} - {s['name']} - {s['dob']}")

def list_courses():
    print("\n=== Courses List ===")
    for c in courses:
        print(f"{c['id']} - {c['name']}")

def show_marks():
    course_id = input("Enter course ID to show marks: ")
    if course_id not in marks:
        print("No marks for this course yet.")
        return
    print(f"\nMarks for course {course_id}:")
    for (student_id, mark) in marks[course_id]:
        for s in students:
            if s["id"] == student_id:
                print(f"{s['name']}: {mark}")
                break

print("Student Mark Management")

num_students = input_number_students()
input_student_info(num_students)

num_courses = input_number_courses()
input_course_info(num_courses)

while True:
    print("\n menu")
    print("1. Input marks for a course")
    print("2. List students")
    print("3. List courses")
    print("4. Show marks for a course")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        input_marks()
    elif choice == "2":
        list_students()
    elif choice == "3":
        list_courses()
    elif choice == "4":
        show_marks()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
