

def save_data(database, output_filename="student_db.txt"):
    with open(output_filename, "w") as file_handle:
        for reg_number, student_info in database.items():
            line = f"{reg_number},{student_info['name']},{student_info['branch']},{student_info['marks']},{student_info['grade']}\n"
            file_handle.write(line)
    print("Success: Data has been saved to the file.")

def load_data(input_filename="student_db.txt"):
    db = {}
    try:
        with open(input_filename, "r") as file_handle:
            for line in file_handle:
                parts = line.strip().split(",")
                if len(parts) == 5:  
                    reg_number = parts[0]
                    db[reg_number] = {
                        "name": parts[1],
                        "branch": parts[2],
                        "marks": float(parts[3]),
                        "grade": parts[4]
                    }
        print("Success: Data has been loaded from the file.")
    except FileNotFoundError:
        print("Notice: No previous data found. Starting with a fresh database.")
    return db