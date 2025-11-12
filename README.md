Python Attendance Tracker
Course Details :-
-Program :- MCA (AI & ML)  
-Semester :- 1st  
-Course Code :- ETCCPP171  
-Course Name :- Programming for Problem Solving Using Python  
-Faculty :- Ms. Neha Kaushik  
-Assignment No. :- 01  
-Student Name :- Raj Tilak Singh  
-Session :- 2025–26  

Project Overview
This project is a Command-Line Attendance Tracker built in Python to simplify and automate attendance management in schools, colleges, or workplaces.  
The system allows users to:
- Record student attendance with timestamps  
- Validate and prevent duplicate entries  
- Generate formatted attendance summaries  
- (Optional) Calculate absentees  
- (Bonus) Save attendance reports to a .txt file  
This assignment demonstrates Python programming foundations — including input/output, lists, dictionaries, conditionals, loops, and string formatting.

Tasks Implemented
Task 1: Setup & Initialization
- Created folder: attendance_tracker
- Created file: tracker.py
- Added comment header and printed welcome message  
Task 2: Input & Data Collection
- Used input() to accept student names and check-in times  
- Stored data in a dictionary:  
  `python
  attendance = { "Riya Sharma": "09:00 AM" }
Task 3: Data Validation
- Ensured names and timestamps are not empty  
- Prevented duplicate entries  
Task 4: Attendance Summary
- Displayed tabular attendance report using f-strings and alignment  
- Counted total students present  
Task 5: Absentee Validation (Optional)
- Asked total class strength  
- Calculated number of absentees  
- Displayed total present and absent counts  
Task 6: Save Report (Bonus)
- Asked if the user wants to save attendance  
- Wrote report to attendance_log.txt with current date & time  

Learning Outcomes
By completing this project, I learned how to:
- Use Python dictionaries to store and manage records  
- Apply control flow (if, elif, else) for validation  
- Use loops for iterative data entry  
- Format clean and readable console outputs  
- Work with file handling and datetime modules  

How to Run the Program
1. Create a folder named attendance_tracker.  
2. Save the Python file as tracker.py inside it.  
3. Open a terminal or IDE and run:
   bash
   python tracker.py
   
4. Follow on-screen instructions to record attendance.

---

Sample Output


==============================================
    Welcome to the Python Attendance Tracker
==============================================
This tool helps record and summarize daily attendance.

How many attendance entries do you want to record? 3

Entry 1 of 3:
Enter student name: Riya Sharma
Enter check-in time (e.g., 09:15 AM): 09:00 AM

Entry 2 of 3:
Enter student name: Arjun Singh
Enter check-in time (e.g., 09:15 AM): 09:10 AM

Entry 3 of 3:
Enter student name: Meena Verma
Enter check-in time (e.g., 09:15 AM): 09:15 AM

==============================================
            Attendance Summary
==============================================
Student Name        Check-in Time
----------------------------------------------
Riya Sharma         09:00 AM
Arjun Singh         09:10 AM
Meena Verma         09:15 AM
----------------------------------------------
Total Students Present: 3

Do you want to calculate absentees? (yes/no): yes
Enter total number of students in class: 5

 Total Present: 3
 Total Absent: 2

Do you want to save the attendance report to a file? (yes/no): yes
Attendance report saved successfully as 'attendance_log.txt'!

 Thank you for using the Python Attendance Tracker!

File Structure

attendance_tracker/
|--tracker.py
|--attendance_log.txt     # (Generated after saving)
|--README.md

Example attendance_log.txt

Attendance Report
Date: 11-11-2025 20:05:24
------------------------------------------
Student Name        Check-in Time
------------------------------------------
Riya Sharma         09:00 AM
Arjun Singh         09:10 AM
Meena Verma         09:15 AM
------------------------------------------
Total Present: 3
Total Absent: 2
