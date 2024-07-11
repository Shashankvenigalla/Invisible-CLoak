import datetime
import openpyxl
from openpyxl.utils import get_column_letter

# Load the Excel workbook and worksheet
wb = openpyxl.load_workbook('attendance.xlsx')
ws = wb.active

# Get the next available column number
next_col = ws.max_column + 1

# Take attendance for each student
date = datetime.date.today()
print(f"Attendance for {date}:")
ws.cell(row=1, column=next_col, value=date)

for row_idx, row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True)):
    reg_num, name = row[:2]
    attendance = input(f"Enter attendance for {name} ({reg_num}): (p)resent or (a)bsent: ")
    if attendance.lower() == "p":
        ws.cell(row=row_idx + 2, column=next_col, value=1)
        ws.cell(row=row_idx + 2, column=3, value=ws.cell(row=row_idx + 2, column=3).value + 1)
    elif attendance.lower() == "a":
        ws.cell(row=row_idx + 2, column=next_col, value=0)
    else:
        print("Invalid input. Please enter 'p' or 'a'.")

# Calculate attendance percentage
# for row_idx, row in enumerate(ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True)):
#     reg_num, name = row[:2]
#     total_classes = ws.max_column - 2
#     present_classes = sum([cell.value for cell in ws[row_idx + 2][2:]])
#     attendance_percentage = (present_classes / total_classes) * 100
#     ws.cell(row=row_idx + 2, column=next_col + 1, value=attendance_percentage)

# Save the Excel workbook
wb.save('attendance.xlsx')

print("\nAttendance updated successfully!")