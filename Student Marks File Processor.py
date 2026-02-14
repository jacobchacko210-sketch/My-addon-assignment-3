import os

def process_marks_file():
    print("--- Student Marks File Processor ---")
    filename = input("Enter the filename (e.g., marks.txt): ").strip()

    valid_records = 0
    invalid_records = 0
    total_marks = 0

    try:
        if os.path.getsize(filename) == 0:
            raise EOFError("File is empty.")
        with open(filename, 'r') as file:
            print(f"\nProcessing '{filename}'...\n")
            print(f"{'Name':<15} | {'Marks':<5} | {'Status'}")
            print("-" * 35)

            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    if ',' not in line:
                        raise ValueError("Missing comma format")

                    parts = line.split(',')
                    
                    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
                         raise ValueError("Incomplete data")

                    name = parts[0].strip()
                    marks_str = parts[1].strip()

                    if not marks_str.isdigit():
                        raise ValueError(f"Invalid marks '{marks_str}'")

                    marks = int(marks_str)
                    
                    total_marks += marks
                    valid_records += 1
                    print(f"{name:<15} | {marks:<5} |  Valid")

                except ValueError as ve:
                    invalid_records += 1
                    print(f"{line:<15} | {'N/A':<5} |  Invalid ({ve})")

        print("\n" + "="*35)
        print("          SUMMARY REPORT          ")
        print("="*35)
        print(f"Total Records Processed : {valid_records + invalid_records}")
        print(f" Valid Records        : {valid_records}")
        print(f" Invalid Records      : {invalid_records}")
        if valid_records > 0:
            average = total_marks / valid_records
            print(f" Class Average        : {average:.2f}")
        else:
            print(" Class Average        : 0.00 (No valid data)")
    except FileNotFoundError:
        print(f"\n Error: The file '{filename}' was not found.")
    except EOFError:
        print(f"\n Error: The file '{filename}' is empty.")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")

if __name__ == "__main__":
    with open("test_marks.txt", "w") as f:
        f.write("Rahul,80\n")
        f.write("Anu,90\n")
        f.write("Arjun,abc\n") 
        f.write("Sneha,95\n")
        f.write("BrokenFormat\n")
    
    print("(A test file 'test_marks.txt' has been created for you)")
    process_marks_file()