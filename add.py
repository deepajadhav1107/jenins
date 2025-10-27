# student_details.py
# Program to display student details
import sys

def display_student_details(name, roll_no, marks):
    print("\n=== Student Details ===")
    print(f"Name       : {name}")
    print(f"Roll No.    : {roll_no}")
    print(f"Marks       : {marks}")
    print("========================")

if __name__ == "__main__":
    print("=== Student Details Program ===")

    try:
        if len(sys.argv) == 4:
            # Case 1: Arguments passed (from Jenkins or CLI)
            name = sys.argv[1]
            roll_no = sys.argv[2]
            marks = float(sys.argv[3])
        else:
            # Case 2: No arguments passed (manual console input)
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            marks = float(input("Enter marks: "))

        display_student_details(name, roll_no, marks)

    except ValueError:
        print("Invalid input! Please enter correct data types.")
