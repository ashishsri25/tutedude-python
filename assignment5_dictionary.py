student_details = {"Alice":70,"Mark":60}
student_name = input("Enter student's name: ")
if student_name in student_details:
    print(f"{student_name} marks: {student_details[student_name]}")
else:
    print(f"{student_name} is not found")