import streamlit as st
from main import Student, StudentManager

 
st.set_page_config(
    page_title="Student Performance Management System",
    page_icon="🎓",
    layout="wide"
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 1.5rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }

        div[data-testid="stMetric"] {
            padding: 0.9rem 1rem;
            border: 1px solid rgba(128, 128, 128, 0.18);
            border-radius: 10px;
        }

        div.stButton > button {
            min-height: 44px;
            border-radius: 8px;
        }

        div[data-testid="stForm"] {
            padding: 1rem 1.1rem;
            border: 1px solid rgba(128, 128, 128, 0.18);
            border-radius: 10px;
        }

        .section-space {
            margin-top: 1.3rem;
            margin-bottom: 1.3rem;
        }

        .app-footer {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(128, 128, 128, 0.18);
            text-align: center;
            opacity: 0.7;
            font-size: 0.85rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎓 Student Performance Management System")
st.caption("A clean student record and performance management interface")

 
def parse_id(value):
    """Convert Student ID input into a positive integer."""
    try:
        value = int(str(value).strip())
        return value if value > 0 else None
    except (ValueError, TypeError):
        return None


def subjects_from(text):
    """Convert comma-separated subjects into a clean list."""
    return [item.strip() for item in str(text).split(",") if item.strip()]


def marks_from(text):
    """Convert comma-separated marks into a validated list."""
    try:
        values = [
            float(item.strip())
            for item in str(text).split(",")
            if item.strip()
        ]
    except ValueError:
        return None

    if not values or any(mark < 0 or mark > 100 for mark in values):
        return None

    return values


def find_student(manager, student_id=None, name=None):
    """Find a student by ID or name."""
    for student in manager.students:
        if student_id is not None and student.student_id == student_id:
            return student

        if name and student.name.strip().lower() == name.strip().lower():
            return student

    return None


def student_rows(students):
    """Create table-ready data for students."""
    return [
        {
            "Student ID": student.student_id,
            "Name": student.name,
            "Age": student.age,
            "Course": student.course,
            "Subjects": len(student.subjects),
            "Attendance": student.attendance,
            "Percentage": round(student.percentage, 2)
        }
        for student in students
    ]


def student_options(manager):
    """Create selectbox options for students."""
    return {
        f"{student.student_id} - {student.name}": student.student_id
        for student in manager.students
    }


def save_data(manager):
    """Save student records using the backend manager."""
    manager.save_data()


def show_student_selector(manager, key):
    """Show student selector and return the selected Student object."""
    options = student_options(manager)
    selected_label = st.selectbox(
        "Select Student",
        list(options.keys()),
        key=key
    )

    return find_student(
        manager,
        student_id=options[selected_label]
    )


def show_dashboard(manager):
    """Display the dashboard."""
    st.subheader("Dashboard")
    st.caption("Overview of student records and overall class performance")

    total_students = len(manager.students)

    average_percentage = (
        round(
            sum(student.percentage for student in manager.students)
            / total_students,
            2
        )
        if total_students
        else 0
    )

    average_attendance = (
        round(
            sum(student.attendance for student in manager.students)
            / total_students,
            2
        )
        if total_students
        else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students", total_students)

    with col2:
        st.metric("Average Percentage", f"{average_percentage}%")

    with col3:
        st.metric("Average Attendance", f"{average_attendance}%")

    st.write("")

    if manager.students:
        st.dataframe(
            student_rows(manager.students),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Student record not found.")

 
manager = StudentManager()
manager.load_data()


 
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

if "selected_option" not in st.session_state:
    st.session_state.selected_option = "Dashboard"

 
if not st.session_state.menu_open:
    show_dashboard(manager)

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

    if st.button("☰ Open Menu", use_container_width=True):
        st.session_state.menu_open = True
        st.rerun()

    st.stop()

 
menu_options = [
    "Dashboard",
    "Add Student",
    "View Students",
    "Search Student",
    "Update Student",
    "Remove Student",
    "Marks Analysis",
    "Grade / Pass-Fail",
    "Attendance",
    "Class Statistics",
    "Top Performers",
    "Save Data"
]

st.subheader("Menu")
st.caption("Select an operation to manage student records")

menu_col, close_col = st.columns([5, 1])

with menu_col:
    selected = st.selectbox(
        "Select Option",
        menu_options,
        index=menu_options.index(st.session_state.selected_option)
    )
    st.session_state.selected_option = selected

with close_col:
    st.write("")
    if st.button("✕ Close", use_container_width=True):
        st.session_state.menu_open = False
        st.session_state.selected_option = "Dashboard"
        st.rerun()

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)



if selected == "Dashboard":
    show_dashboard(manager)


 
elif selected == "Add Student":
    st.subheader("Add Student")
    st.write("")

    with st.form("add_form"):
        left, right = st.columns(2)

        with left:
            student_id_text = st.text_input("Student ID")
            name = st.text_input("Student Name")
            age = st.number_input(
                "Student Age",
                min_value=1,
                max_value=100,
                value=18
            )
            course = st.text_input("Course")

        with right:
            subject_text = st.text_input(
                "Subjects",
                placeholder="Python, SQL, Excel"
            )
            marks_text = st.text_input(
                "Marks",
                placeholder="78, 85, 90"
            )
            attendance = st.number_input(
                "Attendance (%)",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                step=0.5
            )

        st.write("")
        submit = st.form_submit_button(
            "Add Student",
            use_container_width=True
        )

    if submit:
        student_id = parse_id(student_id_text)
        subjects = subjects_from(subject_text)
        marks = marks_from(marks_text)

        if student_id is None:
            st.error("Enter a valid Student ID.")
        elif not name.strip():
            st.error("Enter Student Name.")
        elif not course.strip():
            st.error("Enter Course.")
        elif not subjects:
            st.error("Enter at least one subject.")
        elif marks is None:
            st.error("Marks must be numbers between 0 and 100.")
        elif len(subjects) != len(marks):
            st.error("Number of subjects and marks must be the same.")
        elif find_student(manager, student_id=student_id):
            st.error("Student ID already exists.")
        else:
            student = Student(
                student_id,
                name.strip(),
                int(age),
                course.strip(),
                subjects,
                marks,
                float(attendance)
            )

            manager.students.append(student)
            save_data(manager)
            st.success("Student added successfully.")


 
elif selected == "View Students":
    st.subheader("View Students")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        st.dataframe(
            student_rows(manager.students),
            use_container_width=True,
            hide_index=True
        )

        st.write("")
        student = show_student_selector(manager, "view_student")

        if student:
            st.write("")
            left, right = st.columns(2)

            with left:
                st.write(f"**Student ID:** {student.student_id}")
                st.write(f"**Student Name:** {student.name}")
                st.write(f"**Age:** {student.age}")
                st.write(f"**Course:** {student.course}")
                st.write(f"**Subjects:** {', '.join(student.subjects)}")

            with right:
                st.write(
                    f"**Marks:** {', '.join(map(str, student.marks))}"
                )
                st.write(f"**Attendance:** {student.attendance}%")
                st.write(f"**Percentage:** {student.percentage}%")

 
elif selected == "Search Student":
    st.subheader("Search Student")
    st.write("")

    mode = st.radio(
        "Search By",
        ["Student ID", "Student Name"],
        horizontal=True
    )

    search_value = st.text_input(
        "Enter Student ID"
        if mode == "Student ID"
        else "Enter Student Name"
    )

    st.write("")

    if st.button("Search", use_container_width=True):
        if mode == "Student ID":
            student = find_student(
                manager,
                student_id=parse_id(search_value)
            )
        else:
            student = find_student(
                manager,
                name=search_value
            )

        if student:
            st.success("Student found.")
            st.dataframe(
                student_rows([student]),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("Student record not found.")

 
elif selected == "Update Student":
    st.subheader("Update Student")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        student = show_student_selector(manager, "update_student")
        st.write("")

        with st.form("update_form"):
            left, right = st.columns(2)

            with left:
                name = st.text_input(
                    "Student Name",
                    value=student.name
                )
                age = st.number_input(
                    "Student Age",
                    min_value=1,
                    max_value=100,
                    value=int(student.age)
                )
                course = st.text_input(
                    "Course",
                    value=student.course
                )

            with right:
                subject_text = st.text_input(
                    "Subjects",
                    value=", ".join(student.subjects)
                )
                marks_text = st.text_input(
                    "Marks",
                    value=", ".join(map(str, student.marks))
                )
                attendance = st.number_input(
                    "Attendance (%)",
                    min_value=0.0,
                    max_value=100.0,
                    value=float(student.attendance),
                    step=0.5
                )

            st.write("")
            submit = st.form_submit_button(
                "Update Student",
                use_container_width=True
            )

        if submit:
            subjects = subjects_from(subject_text)
            marks = marks_from(marks_text)

            if not name.strip():
                st.error("Enter Student Name.")
            elif not course.strip():
                st.error("Enter Course.")
            elif not subjects:
                st.error("Enter at least one subject.")
            elif marks is None:
                st.error("Marks must be numbers between 0 and 100.")
            elif len(subjects) != len(marks):
                st.error("Number of subjects and marks must be the same.")
            else:
                student.name = name.strip()
                student.age = int(age)
                student.course = course.strip()
                student.subjects = subjects
                student.marks = marks
                student.attendance = float(attendance)

                save_data(manager)
                st.success("Student updated successfully.")

 
elif selected == "Remove Student":
    st.subheader("Remove Student")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        student = show_student_selector(manager, "remove_student")
        st.write("")
        st.warning(
            f"Selected Student: {student.name} "
            f"(ID: {student.student_id})"
        )

        st.write("")

        if st.button(
            "Remove Student",
            type="primary",
            use_container_width=True
        ):
            manager.students.remove(student)
            save_data(manager)
            st.success("Student removed successfully.")
            st.rerun()

 
elif selected == "Marks Analysis":
    st.subheader("Marks Analysis")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        student = show_student_selector(manager, "marks_student")
        st.write("")

        total_marks = sum(student.marks)
        highest_marks = max(student.marks)
        lowest_marks = min(student.marks)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Marks", round(total_marks, 2))

        with col2:
            st.metric("Average", f"{student.percentage}%")

        with col3:
            st.metric("Highest", round(highest_marks, 2))

        with col4:
            st.metric("Lowest", round(lowest_marks, 2))

        st.write("")
        st.dataframe(
            {
                "Subject": student.subjects,
                "Marks": student.marks
            },
            use_container_width=True,
            hide_index=True
        )

 
elif selected == "Grade / Pass-Fail":
    st.subheader("Grade / Pass-Fail")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        student = show_student_selector(manager, "grade_student")
        st.write("")

        passed = all(mark >= 33 for mark in student.marks)

        if passed:
            st.success("Result: PASS")
        else:
            st.error("Result: FAIL")

        percentage = student.percentage

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

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Percentage", f"{percentage}%")

        with col2:
            st.metric("Grade", grade)
 
elif selected == "Attendance":
    st.subheader("Attendance")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        student = show_student_selector(manager, "attendance_student")
        st.write("")

        st.metric("Attendance", f"{student.attendance}%")

        st.write("")

        if student.attendance < 70:
            st.warning("Short Attendance")
        else:
            st.success("Attendance is satisfactory.")
 
elif selected == "Class Statistics":
    st.subheader("Class Statistics")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        total_students = len(manager.students)

        average_percentage = round(
            sum(student.percentage for student in manager.students)
            / total_students,
            2
        )

        passed_students = sum(
            all(mark >= 33 for mark in student.marks)
            for student in manager.students
        )

        failed_students = total_students - passed_students

        average_attendance = round(
            sum(student.attendance for student in manager.students)
            / total_students,
            2
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Students", total_students)

        with col2:
            st.metric("Average Percentage", f"{average_percentage}%")

        with col3:
            st.metric("Passed", passed_students)

        with col4:
            st.metric("Failed", failed_students)

        st.write("")
        st.write(
            f"Average Attendance: **{average_attendance}%**"
        )


 
elif selected == "Top Performers":
    st.subheader("Top Performers")
    st.write("")

    if not manager.students:
        st.info("Student record not found.")
    else:
        minimum_percentage = st.number_input(
            "Enter Minimum Percentage",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=1.0
        )

        performers = sorted(
            [
                student
                for student in manager.students
                if student.percentage > minimum_percentage
            ],
            key=lambda student: student.percentage,
            reverse=True
        )

        st.write("")

        if performers:
            st.dataframe(
                student_rows(performers),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No student found above this percentage.")

 
elif selected == "Save Data":
    st.subheader("Save Data")
    st.caption("Store the current student records in File.json")

    if st.button("Save Student Data", use_container_width=True):
        save_data(manager)
        st.success("Student data saved successfully.")

    st.write("")
    st.metric("Current Student Records", len(manager.students))


 
st.markdown(
    "<div class=\"app-footer\">Student Performance Management System • Streamlit UI</div>",
    unsafe_allow_html=True
)
