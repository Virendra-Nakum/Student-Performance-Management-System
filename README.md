# Student Performance Management System

A Python and Streamlit based **Student Performance Management System** for managing student records, analyzing academic performance, tracking attendance, and storing student data using JSON file handling.

---

## Project Overview

The Student Performance Management System provides both:

- A Python console-based backend
- A Streamlit web interface

The system allows users to add, view, search, update, remove, and analyze student records through a simple and professional interface.

Student data is stored locally in `File.json`.

---

## Features

### Student Management

- Add Student
- View Students
- Search Student
- Update Student
- Remove Student
- Duplicate Student ID checking

### Academic Performance

- Marks Analysis
- Total Marks
- Average Percentage
- Highest Marks
- Lowest Marks
- Grade Calculation
- Pass / Fail Result
- Top Performers

### Attendance

- Student Attendance Tracking
- Short Attendance Warning
- Attendance threshold below 70%

### Class Statistics

- Total Students
- Average Percentage
- Passed Students
- Failed Students
- Average Attendance

### Data Management

- JSON-based data storage
- Save student records
- Load existing student records
- Input validation
- Error handling

---

## Technologies Used

- Python
- Streamlit
- JSON
- Object-Oriented Programming (OOP)
- Inheritance
- `@property`
- `@staticmethod`
- `@classmethod`
- Lambda Functions
- `filter()`
- Sorting
- Exception Handling
- File Handling

---

## Project Structure

```text
Student-Performance-Management-System/
│
├── main.py
├── app.py
├── File.json
├── requirements.txt
├── .gitignore
└── README.md
````

---

## Files Description

### `main.py`

Contains the main Python backend and console-based Student Performance Management System.

It contains:

* `Student`
* `StudentManager`
* `StudentAnalytics`

The backend handles:

* Student records
* Validation
* Search
* Update
* Remove
* Marks analysis
* Grade / Pass-Fail
* Attendance
* Class statistics
* Top performers
* Save / Load operations

---

### `app.py`

Contains the Streamlit web interface.

The Streamlit application provides:

* Dashboard
* Add Student
* View Students
* Search Student
* Update Student
* Remove Student
* Marks Analysis
* Grade / Pass-Fail
* Attendance
* Class Statistics
* Top Performers
* Save Data

---

### `File.json`

Stores student records in JSON format.

Example:

```json
[]
```

The file can contain student records after students are added through the application.

---

### `requirements.txt`

Contains the Python package required to run the Streamlit application.

```text
streamlit
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Student-Performance-Management-System
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit Application

Use:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Run the Console Application

The original Python console application can also be started using:

```bash
python main.py
```

---

## Streamlit Dashboard

The application starts with a dashboard showing:

* Total Students
* Average Percentage
* Average Attendance
* Student records

The menu can be opened when required.

---

## Student Input Format

### Subjects

Subjects should be entered using commas.

Example:

```text
Python, SQL, Excel
```

### Marks

Marks should also be entered using commas.

Example:

```text
78, 85, 90
```

The number of subjects and marks must be the same.

---

## Validation

The application validates:

* Student ID
* Duplicate Student ID
* Student Name
* Student Age
* Course
* Subjects
* Marks
* Attendance
* Search input
* Student records

### Marks

Marks must be between:

```text
0 - 100
```

### Attendance

Attendance must be between:

```text
0 - 100
```

### Student ID

Student ID must be a positive integer and must be unique.

---

## Passing Rule

A student passes when **every subject has marks of 33 or above**.

If any subject has marks below 33, the student is marked as:

```text
FAIL
```

---

## Grading System

| Percentage | Grade |
| ---------- | ----- |
| 90+        | A+    |
| 80–89.99   | A     |
| 70–79.99   | B+    |
| 60–69.99   | B     |
| 50–59.99   | C     |
| 40–49.99   | D     |
| Below 40   | E     |

---

## Attendance Rule

Students with attendance below **70%** are identified as:

```text
Short Attendance
```

---

## Top Performers

The Top Performers section allows the user to enter a minimum percentage.

Students whose percentage is **greater than** the selected percentage are displayed in descending order.

---

## Data Storage

Student records are stored locally in:

```text
File.json
```

The application uses Python's built-in `json` module for storing and loading data.

---

## OOP Structure

### Student

Represents an individual student.

Stores:

* Student ID
* Name
* Age
* Course
* Subjects
* Marks
* Attendance
* Percentage

### StudentManager

Handles:

* Adding students
* Viewing students
* Searching students
* Updating students
* Removing students
* Login/account operations
* Saving and loading data

### StudentAnalytics

Inherits from `StudentManager` and provides:

* Marks Analysis
* Grade / Pass-Fail
* Attendance Analysis
* Class Statistics
* Top Performers

---

## Error Handling

The project includes validation and error handling to prevent common invalid inputs from crashing the application.

Examples include:

* Invalid Student ID
* Duplicate Student ID
* Invalid marks
* Invalid attendance
* Missing student records
* Invalid subject/marks count
* Invalid stored JSON data

---

## Application Menu

The Streamlit application provides the following operations:

```text
Dashboard
Add Student
View Students
Search Student
Update Student
Remove Student
Marks Analysis
Grade / Pass-Fail
Attendance
Class Statistics
Top Performers
Save Data
```

---

 
Aspiring Data Analyst & Data Scientist

```text
Python | SQL | Machine Learning | Data Analytics | AI/ML
```

---

## Project Status

**Completed**

The project currently includes:

* Python backend
* Streamlit web interface
* Student management
* Performance analysis
* Attendance management
* Class statistics
* JSON data storage
* Input validation
* Error handling
* GitHub-ready project structure


## Author

**Virendra Nakum**