"""" DATA VALIDATION """
data_valid = False
while data_valid == False:
    grade_1 = float(input("Type the grade of the first test:"))
    if grade_1 < 0 or grade_1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade_2 = float(input("Type the grade of the second test:"))
    if grade_2 < 0 or grade_2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = int(input("Type total number of classes:"))
    if total_classes <= 0:
        print("The number of classes can not be zero or less")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = int(input("Type the number of absences:"))
    if absences < 0 or absences > total_classes:
        print("The number of absences can not be less than zero or greater than the total classes")
        continue
    else:
        data_valid = True

Avg_grade = (grade_1 + grade_2) / 2
attendance = (total_classes - absences) / total_classes
print("Average grade:",round(Avg_grade,2))
"""Another way to print avg_grade"""
print(f"Average grade: {round(Avg_grade,3)}")
print("Attendance rate:", str(round(attendance * 100)) + "%")
""" Another way to print Attendance rate"""
print(f"Attendance rate: {round(attendance * 100,2)}%")
if (Avg_grade >= 6 and attendance >= 0.8):
    print("The student has been approved.Congratulations!")
elif (Avg_grade < 6 and attendance < 0.8):
    print("The student has failed due to an average grade lower than 6.0 and attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an attendance rate lower than 80%.")