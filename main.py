# -------------------------------------------------------------
# Name: Raj Tilak Singh
# Date: 13-Nov-2025
# Assignment Title: Command-Line Attendance Tracker
# Course: MCA (AI & ML) - Programming for Problem Solving Using Python
# Faculty: Ms. Neha Kaushik
# -------------------------------------------------------------

# Importing required module
from datetime import datetime

print("==============================================")
print("   Welcome to the Python Attendance Tracker ")
print("==============================================")
print("This tool helps record and summarize daily attendance.\n")

# Initialize attendance dictionary
attendance = {}

# ---------------- Task 2: Input & Data Collection ----------------

while True:
    try:
        total_entrys = int(input("How many attendance entries do you want to record? "))
        if total_entrys <= 0:
            print("Please enter a valid positive number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

# Collect student data
for i in range(total_entrys):
    print(f"\nEntry {i+1} of {total_entrys}:")
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be empty. Please try again.")
            continue
        if name in attendance:
            print("This name already exists! Duplicate entry not allowed.")
            continue
        break

    while True:
        time = input("Enter check-in time (e.g., 09:15 AM): ").strip()
        if time == "":
            print("Check-in time cannot be empty. Please try again.")
            continue
        break

    # Store in dictionary
    attendance[name] = time

# ---------------- Task 4: Attendance Summary ----------------
print("\n==============================================")
print("            Attendance Summary")
print("==============================================")
print(f"{'Student Name':<20} {'Check-in Time':<15}")
print("----------------------------------------------")

for student, checkin in attendance.items():
    print(f"{student:<20} {checkin:<15}")

print("----------------------------------------------")
print(f"Total Students Present: {len(attendance)}")

# ---------------- Task 5: Absentee Validation (Optional) ----------------
while True:
    choice = input("\nDo you want to calculate absentees? (yes/no): ").strip().lower()
    if choice in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'.")

total_absent = 0
if choice == 'yes':
    while True:
        try:
            total_students = int(input("Enter total number of students in class: "))
            if total_students < len(attendance):
                print("Total students cannot be less than present students.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    total_absent = total_students - len(attendance)
    print(f"\nTotal Present: {len(attendance)}")
    print(f"Total Absent: {total_absent}")

# ---------------- Task 6: Save Attendance Report (Bonus) ----------------
save_choice = input("\nDo you want to save the attendance report to a file? (yes/no): ").strip().lower()
if save_choice == 'yes':
    with open("attendance_log.txt", "w") as file:
        file.write("Attendance Report\n")
        file.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write("------------------------------------------\n")
        file.write(f"{'Student Name':<20} {'Check-in Time':<15}\n")
        file.write("------------------------------------------\n")
        for student, checkin in attendance.items():
            file.write(f"{student:<20} {checkin:<15}\n")
        file.write("------------------------------------------\n")
        file.write(f"Total Present: {len(attendance)}\n")
        if total_absent:
            file.write(f"Total Absent: {total_absent}\n")
    print("\nAttendance report saved successfully as 'attendance_log.txt'!")

print("\nThank you for using the Python Attendance Tracker!")
print("==============================================")
