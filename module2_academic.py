

def determine_grade(marks):
    
    if marks < 33:
        return "F"
    elif 33 <= marks <= 40:
        return "E"
    elif 41 <= marks <= 60:
        return "D"
    elif 61 <= marks <= 80:
        return "C"
    elif 81 <= marks <= 90:
        return "B"
    elif 91 <= marks <= 100:
        return "A"
    else:
        return "Invalid"

def update_marks(database, registration_number, marks):
    # Check if the student exists in the database
    if registration_number in database:
        if 0 <= marks <= 100:
            database[registration_number]["marks"] = marks
            database[registration_number]["grade"] = determine_grade(marks)
            print("Success! Marks and Grade have been updated.")
        else:
            print("Oops! Marks should be between 0 and 100.")
    else:
        print("Error: Student not found in the database.")

def display_report(database):
    print("\n=== ACADEMIC GRADE REPORT ===")
    total_students = 0
    for registration_number, info in database.items():
        if info["marks"] != -1:  
            print(f"Reg No: {registration_number} | Name: {info['name']} | Marks: {info['marks']} | Grade: {info['grade']}")
            total_students += 1
    if total_students == 0:
        print("No academic data available yet.")
    print("=============================\n")