# Student Management System

A simple **Student Management System made using Python**.  
This project is a basic console-based program that helps manage student details, marks, grades, and academic reports.

## About the Project

I made this project to practice Python concepts like:

- Functions
- Dictionaries
- Loops and conditions
- Multiple Python modules
- File handling
- Exception handling
- Basic CRUD operations

The program works through a simple menu where the user can choose what they want to do.

## Features

The program currently provides these options:

1. **Create Student** – Add a new student with their registration number, name and branch.
2. **Read Student** – View the details of an existing student.
3. **Update Student** – Change the student's name or branch.
4. **Delete Student** – Remove a student from the system.
5. **Input Marks & Generate Grade** – Enter marks and automatically calculate the grade.
6. **Generate Academic Report** – Display the marks and grades of students.
7. **Save Data** – Save student information to a file.
8. **Exit** – Save the data and close the program.

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── module1_crud.py
├── module2_academic.py
├── module3_storage.py
└── student_db.txt
```

### What each file does

**main.py**  
Contains the main menu and controls the overall flow of the program.

**module1_crud.py**  
Handles basic student operations such as creating, reading, updating and deleting records.

**module2_academic.py**  
Handles marks, grade calculation and generating the academic report.

**module3_storage.py**  
Handles saving student data to a file and loading it again when the program starts.

**student_db.txt**  
Stores the student data so that it is not lost when the program is closed.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project folder

```bash
cd Student-Management-System
```

### 3. Run the program

```bash
python main.py
```

The program will then show a menu like:

```text
--- Student Management System ---

1. Create Student
2. Read Student
3. Update Student
4. Delete Student
5. Input Marks & Generate Grade
6. Generate Academic Report
7. Save Data
8. Exit

Enter your choice (1-8):
```

## Example

For example, while creating a student, the program asks:

```text
Enter Registration No: 101
Enter Name: Rahul
Enter Branch: CSE
```

After entering marks, the program calculates the grade automatically.

## Grade System

The program uses the following grading system:

| Marks | Grade |
|---|---|
| 0–32 | F |
| 33–40 | E |
| 41–60 | D |
| 61–80 | C |
| 81–90 | B |
| 91–100 | A |

## Concepts Used

Some of the main Python concepts used in this project are:

- `if-elif-else`
- `while` loop
- Functions
- Dictionaries
- Modules
- `try-except`
- File reading and writing
- User input
- Basic CRUD operations

## Future Improvements

There are a few things that can be added later:

- A graphical user interface
- SQLite/database support
- Login system
- Multiple subjects for each student
- CGPA calculation
- Search and sorting options
- Exporting reports to PDF or Excel

## Note

This is a **student-level Python project** made mainly for learning and understanding how different Python concepts can be combined into one application.

More features and improvements can be added as I learn more Python.

## Author

**Vansham Singh**

Student | Learning Python & AI/ML