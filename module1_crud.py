

def create_student(database, registration_number, student_name, student_branch):
    if registration_number in database:
        print("Oops! A student with this registration number already exists.")
        return
    database[registration_number] = {
        "name": student_name,
        "branch": student_branch,
        "marks": -1,
        "grade": "N/A"
    }
    print("Great! Student has been created.")

def read_student(database, registration_number):
    if registration_number in database:
        student_info = database[registration_number]
        print("\n--- Student Details ---")
        print(f"Reg No: {registration_number}\nName: {student_info['name']}\nBranch: {student_info['branch']}")
        if student_info['marks'] != -1:
            print(f"Marks: {student_info['marks']}\nGrade: {student_info['grade']}")
        print("-----------------------")
    else:
        print("Sorry, we couldn't find that student.")

def update_student(database, registration_number, new_name, new_branch):
    if registration_number in database:
        if new_name:  
            database[registration_number]["name"] = new_name
        if new_branch:  
            database[registration_number]["branch"] = new_branch
        print("Awesome! Student info updated.")
    else:
        print("Sorry, we couldn't find that student.")

def delete_student(database, registration_number):
    if registration_number in database:
        del database[registration_number]
        print("Done! Student has been deleted.")
    else:
        print("Sorry, we couldn't find that student.")