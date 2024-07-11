# Initialize an empty dictionary to store student information
students = {}

# Add students to the dictionary with empty slots for daily attendance and overall percentage
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input(f"Enter student {i+1} name: ")
    reg_num = input(f"Enter student {i+1} registration number: ")
    students[reg_num] = {"name": name, "attendance": [], "overall_percentage": 0}

# Take attendance for each student
import datetime
date = datetime.date.today()
print(f"Attendance for {date}:")
for reg_num, student in students.items():
    attendance = input(f"Enter attendance for {student['name']} ({reg_num}): (p)resent or (a)bsent: ")
    if attendance.lower() == "p":
        students[reg_num]["attendance"].append({"date": date, "status": "present"})
    elif attendance.lower() == "a":
        students[reg_num]["attendance"].append({"date": date, "status": "absent"})
    else:
        print("Invalid input. Please enter 'p' or 'a'.")

# Print updated student information
print("\nUpdated student information:")
for reg_num, student in students.items():
    print(f"Name: {student['name']}, Registration Number: {reg_num}, Attendance: {student['attendance']}")