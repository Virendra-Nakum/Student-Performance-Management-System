import json

print("----- WELCOME TO STUDENT PERFORMANCE MANAGEMENT SYSTEM -----")

class Student:

    def __init__(self, student_id, name, age, course, subjects, marks, attendance):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.subjects = subjects
        self.marks = marks
        self.attendance = attendance

    @property
    def percentage(self):
        return round(sum(self.marks) / len(self.marks), 2) if self.marks else 0

    @staticmethod
    def valid_marks(mark):
        return 0 <= mark <= 100

    def get_data(self):
        return {
            "Student ID": self.student_id,
            "Student Name": self.name,
            "Student Age": self.age,
            "Course": self.course,
            "Number of Subject": len(self.subjects),
            "Subject Name": self.subjects,
            "Marks": self.marks,
            "Attendance": self.attendance,
            "Percentage": self.percentage
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["Student ID"],
            data["Student Name"],
            data["Student Age"],
            data["Course"],
            data["Subject Name"],
            data["Marks"],
            data["Attendance"]
        )

    def display(self):
        print("Student ID:"        , self.student_id)
        print("Student Name:"      , self.name)
        print("Student Age:"       , self.age)
        print("Course:"            , self.course)
        print("Number of Subjects:", len(self.subjects))
        print("Subject Names:"     , self.subjects)
        print("Marks:"             , self.marks)
        print("Attendance:"        , self.attendance, "%")
        print("Percentage:"        , self.percentage, "%")
        print("------------------------")
 
class StudentManager:

    def __init__(self):
        self.students = []
        self.username = None
        self.password = None

    def add_student(self):
        while True:
            try:
                student_id = int(input("Enter Student ID:- "))

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

                if any(i.student_id == student_id for i in self.students):
                    print("Student ID already exists.")
                    continue

                break

            except ValueError:
                print("Enter a valid Student ID.")

        while True:
            name = input("Enter Student Name:- ").strip()

            if name:
                break

            print("Enter a valid Student Name.")

        while True:
            try:
                age = int(input("Enter Student Age:- "))

                if age <= 0:
                    print("Enter a valid Student Age.")
                    continue

                break

            except ValueError:
                print("Enter a valid Student Age.")

        while True:
            course = input("Enter Course Name:- ").strip()

            if course:
                break

            print("Enter a valid Course Name.")

        while True:
            try:
                num = int(input("Enter Subject Number:- "))

                if num <= 0:
                    print("Subject Number must be greater than 0.")
                    continue

                subject = input("Enter Subject Name (separated by space):- ").split()

                if num == len(subject):
                    break

                print("Number of subjects and subject names do not match.")

            except ValueError:
                print("Enter a valid Subject Number.")

        mark = []

        for sub in subject:
            while True:
                try:
                    marks = int(input(f"Enter {sub} Marks:- "))

                    if not Student.valid_marks(marks):
                        print("Marks must be between 0 and 100.")
                        continue

                    mark.append(marks)
                    break

                except ValueError:
                    print("Enter valid Marks.")

        while True:
            try:
                atd = int(input("Enter Student Attendance:- "))

                if atd < 0 or atd > 100:
                    print("Attendance must be between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Enter valid Attendance.")

        student = Student(student_id, name, age, course, subject, mark, atd)
        self.students.append(student)

        print("Student Added Successfully!")
        print("------------------------")

    def display_student(self):
        if not self.students:
            print("Student record not found.")
            return

        for student in self.students:
            student.display()

    # Python-style overloading using default argument
    def search_student(self, student_id=None, name=None):
        if not self.students:
            print("Student record not found.")
            return None

        if student_id is None and name is None:
            while True:
                try:
                    student_id = int(input("Enter Student ID:- "))
                    break
                except ValueError:
                    print("Enter a valid Student ID.")

        for student in self.students:
            if student_id is not None and student.student_id == student_id:
                return student

            if name is not None and student.name.lower() == name.lower():
                return student

        print("Student record not found.")
        return None

    def remove_student(self):
        student = self.search_student()

        if student is None:
            return

        self.students.remove(student)
        print("Student Removed Successfully.")

    def update_info(self):
        if not self.students:
            print("Student record not found.")
            return

        student = self.search_student()

        if student is None:
            return

        print("Update Information")
        print("1. Name")
        print("2. Age")
        print("3. Course")
        print("4. Subject")
        print("5. Marks")
        print("6. Attendance")

        while True:
            try:
                choice = int(input("Enter Your Choice:- "))

                if 1 <= choice <= 6:
                    break

                print("Enter a valid choice.")

            except ValueError:
                print("Enter a valid choice.")

        if choice == 1:
            while True:
                name = input("Update Student Name:- ").strip()

                if name:
                    student.name = name
                    break

                print("Enter a valid Student Name.")

        elif choice == 2:
            while True:
                try:
                    age = int(input("Update Student Age:- "))

                    if age <= 0:
                        print("Enter a valid Student Age.")
                        continue

                    student.age = age
                    break

                except ValueError:
                    print("Enter a valid Student Age.")

        elif choice == 3:
            while True:
                course = input("Update Course Name:- ").strip()

                if course:
                    student.course = course
                    break

                print("Enter a valid Course Name.")

        elif choice == 4:
            while True:
                try:
                    num = int(input("Update Subject Number:- "))

                    if num <= 0:
                        print("Subject Number must be greater than 0.")
                        continue

                    subject = input("Update Subject Names (separated by space):- ").split()

                    if num != len(subject):
                        print("Number of subjects and subject names do not match.")
                        continue

                    mark = []

                    for sub in subject:
                        while True:
                            try:
                                marks = int(input(f"Enter {sub} Marks:- "))

                                if not Student.valid_marks(marks):
                                    print("Marks must be between 0 and 100.")
                                    continue

                                mark.append(marks)
                                break

                            except ValueError:
                                print("Enter valid Marks.")

                    student.subjects = subject
                    student.marks = mark
                    break

                except ValueError:
                    print("Enter a valid Subject Number.")

        elif choice == 5:
            mark = []

            for sub in student.subjects:
                while True:
                    try:
                        marks = int(input(f"Update {sub} Marks:- "))

                        if not Student.valid_marks(marks):
                            print("Marks must be between 0 and 100.")
                            continue

                        mark.append(marks)
                        break

                    except ValueError:
                        print("Enter valid Marks.")

            student.marks = mark

        elif choice == 6:
            while True:
                try:
                    atd = int(input("Update Student Attendance:- "))

                    if atd < 0 or atd > 100:
                        print("Attendance must be between 0 and 100.")
                        continue

                    student.attendance = atd
                    break

                except ValueError:
                    print("Enter valid Attendance.")

        print("Student Information Updated Successfully.")

    def login(self):
        while True:
            print("\n1. Login")
            print("2. Create Account")
            print("3. Change Password")
            print("4. Exit")

            try:
                choice = int(input("Enter Choice:- "))
            except ValueError:
                print("Enter a valid choice.")
                continue

            if choice == 1:
                if self.username is None:
                    print("No account found. Please create an account first.")
                    continue

                user = input("Enter Username:- ")
                pas = input("Enter Password:- ")

                if user == self.username and pas == self.password:
                    print("Login Successful.")
                else:
                    print("Invalid Username or Password.")

            elif choice == 2:
                name = input("Enter Username:- ").strip()

                if not name:
                    print("Username cannot be empty.")
                    continue

                pas = input("Enter Password:- ")
                pas1 = input("Re-enter Password:- ")

                if pas == pas1:
                    self.username = name
                    self.password = pas
                    print("Account Created Successfully.")
                else:
                    print("Passwords do not match.")

            elif choice == 3:
                if self.username is None:
                    print("No account found. Please create an account first.")
                    continue

                user = input("Enter Username:- ")

                if user == self.username:
                    old_password = input("Enter Old Password:- ")

                    if old_password == self.password:
                        new_password = input("Enter New Password:- ")

                        if not new_password:
                            print("Password cannot be empty.")
                            continue

                        self.password = new_password
                        print("Password Changed Successfully.")
                    else:
                        print("Incorrect Password.")
                else:
                    print("Username not found.")

            elif choice == 4:
                print("Thank You!")
                break

            else:
                print("Enter a valid choice.")

    def save_data(self):
        try:
            with open("File.json", "w") as file:
                json.dump([i.get_data() for i in self.students], file, indent=4)

            print("Data Saved Successfully.")

        except OSError as error:
            print("Unable to save student records.")
            print("Error:", error)

    def load_data(self):
        try:
            with open("File.json", "r") as file:
                data = json.load(file)

            if isinstance(data, list):
                self.students = [Student.from_dict(i) for i in data]

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("File contains invalid data.")
            self.students = []

        except OSError:
            print("Unable to load student records.")
            self.students = []
 
class StudentAnalytics(StudentManager):

    # Method overriding
    def search_student(self, student_id=None, name=None):
        return super().search_student(student_id, name)

    def marks_analysis(self):
        student = self.search_student()

        if student is None:
            return

        mark = student.marks

        if not mark:
            print("No marks available for this student.")
            return

        total = sum(mark)
        percentage = total / len(mark)

        print()
        print("Student ID:", student.student_id)
        print("Total Marks:", total)
        print(f"Percentage: {percentage:.2f}%")
        print(f"Average Marks: {percentage:.2f}")
        print("Highest Marks:", max(mark))
        print("Lowest Marks:", min(mark))

        fail_mark = list(filter(lambda x: x < 33, mark))

        if fail_mark:
            print("Failed Subject Marks:", fail_mark)
        else:
            print("Failed Subject Marks: None")

    def grade_pass_fail(self):
        student = self.search_student()

        if student is None:
            return

        mark = student.marks

        if not mark:
            print("No marks available for this student.")
            return

        percentage = sum(mark) / len(mark)

        if not all(x >= 33 for x in mark):
            print(f"Student Name: {student.name}")
            print(f"Percentage: {percentage:.2f}%")
            print("Result: FAIL")
            print("Reason: One or more subjects have marks below 33.")
            return

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "E"

        print(f"Student Name: {student.name}")
        print(f"Percentage: {percentage:.2f}%")
        print("Grade:", grade)
        print("Result: PASS")

    def attendance_analysis(self):
        if not self.students:
            print("Student record not found.")
            return

        data = list(filter(lambda x: x.attendance < 70, self.students))

        if not data:
            print("No student has short attendance.")
            return

        for i in data:
            print("Name:", i.name)
            print("Attendance:", i.attendance, "%")
            print("Notice: Short Attendance")
            print("------------------------")

    def class_statistics(self):
        if not self.students:
            print("Student record not found.")
            return

        percentage = [i.percentage for i in self.students]
        attendance = [i.attendance for i in self.students]

        high = max(self.students, key=lambda x: x.percentage)
        low = min(self.students, key=lambda x: x.percentage)

        passed = sum(all(mark >= 33 for mark in i.marks) for i in self.students)
        failed = len(self.students) - passed

        print("------")
        print("Total Students in This Class:", len(self.students))
        print("------")
        print(f"Average Percentage in This Class: {sum(percentage) / len(percentage):.2f}%")
        print("------")
        print("Highest Score in This Class:", high.name)
        print("Percentage:", high.percentage, "%")
        print("------")
        print("Lowest Score in This Class:", low.name)
        print("Percentage:", low.percentage, "%")
        print("------")
        print("Passed Students:", passed)
        print("------")
        print("Failed Students:", failed)
        print("------")
        print(f"Average Attendance in This Class: {sum(attendance) / len(attendance):.2f}%")
        print("------")

    def top_performers(self):
        if not self.students:
            print("Student record not found.")
            return

        while True:
            try:
                num = float(input("Enter Minimum Percentage:- "))

                if num < 0 or num > 100:
                    print("Percentage must be between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Enter a valid Percentage.")

        data = list(filter(lambda x: x.percentage > num, self.students))

        if not data:
            print("No student found above this percentage.")
            return

        data.sort(key=lambda x: x.percentage, reverse=True)

        for i in data:
            print("Student Name:", i.name)
            print("Percentage:", i.percentage, "%")
 
def main():

    app = StudentAnalytics()
    app.load_data()

    while True:

        print("\n----- STUDENT PERFORMANCE MANAGEMENT SYSTEM -----")
        print("1.  Login")
        print("2.  Add Student")
        print("3.  View Student")
        print("4.  Search Student")
        print("5.  Update Student")
        print("6.  Marks Analysis")
        print("7.  Grade / Pass-Fail")
        print("8.  Attendance")
        print("9.  Class Statistics")
        print("10. Top Performers")
        print("11. Save")
        print("12. Exit")

        try:
            choice = int(input("Enter Your Choice:- "))
        except ValueError:
            print("Enter (1 to 12):")
            continue

        if choice == 1:
            app.login()

        elif choice == 2:
            app.add_student()

        elif choice == 3:
            app.display_student()

        elif choice == 4:
            app.search_student()

        elif choice == 5:
            app.update_info()

        elif choice == 6:
            app.marks_analysis()

        elif choice == 7:
            app.grade_pass_fail()

        elif choice == 8:
            app.attendance_analysis()

        elif choice == 9:
            app.class_statistics()

        elif choice == 10:
            app.top_performers()

        elif choice == 11:
            app.save_data()

        elif choice == 12:
            app.save_data()
            print("Thank You!")
            print("Exiting Program...")
            break

        else:
            print("Enter a valid choice.")


if __name__ == "__main__":
    main()
