# main.py
import module1_crud
import module2_academic
import module3_storage

def main():
    students_db = module3_storage.load_data()

    while True:
        print("\n--- Welcome to the Student Management System ---")
        print("1. Add New Student")
        print("2. View Student Info")
        print("3. Modify Student Details")
        print("4. Remove Student")
        print("5. Enter Marks & Get Grade")
        print("6. Create Academic Report")
        print("7. Save Changes")
        print("8. Exit the Program")
        
        user_choice = input("Please choose an option (1-8): ")

        if user_choice == '1':
            reg_no = input("Enter Registration Number: ")
            student_name = input("Enter Student Name: ")
            student_branch = input("Enter Student Branch: ")
            module1_crud.create_student(students_db, reg_no, student_name, student_branch)
        
        elif user_choice == '2':
            reg_no = input("Enter Registration Number to view: ")
            module1_crud.read_student(students_db, reg_no)
            
        elif user_choice == '3':
            reg_no = input("Enter Registration Number to modify: ")
            new_name = input("Enter new Name (leave blank to keep current): ")
            new_branch = input("Enter new Branch (leave blank to keep current): ")
            module1_crud.update_student(students_db, reg_no, new_name, new_branch)
            
        elif user_choice == '4':
            reg_no = input("Enter Registration Number to remove: ")
            module1_crud.delete_student(students_db, reg_no)
            
        elif user_choice == '5':
            reg_no = input("Enter Registration Number: ")
            try:
                marks_obtained = float(input("Enter marks (0-100): "))
                module2_academic.input_marks(students_db, reg_no, marks_obtained)
            except ValueError:
                print("Oops! Please enter a valid number for the marks.")
                
        elif user_choice == '6':
            module2_academic.generate_report(students_db)
            
        elif user_choice == '7':
            module3_storage.save_data(students_db)
            print("Data saved successfully!")
            
        elif user_choice == '8':
            module3_storage.save_data(students_db)
            print("Thanks for using the system. Goodbye!")
            break
            
        else:
            print("Hmm, that's not a valid option. Please pick a number between 1 and 8.")

if __name__ == "__main__":
    main()