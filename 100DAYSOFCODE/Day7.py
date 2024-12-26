def Grade_calc(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

def gen_marks():
    students = {}
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        name = input("Enter student name: ")
        subjects = int(input(f"Enter number of subjects for {name}: "))
        total_marks = 0
        
        for i in range(subjects):   
            marks = int(input(f"Enter marks for subject {i+1}: "))
            total_marks += marks
        
        percentage = total_marks / subjects
        grade = Grade_calc(percentage)
        students[name] = {
            "Total Marks": total_marks,
            "Percentage": percentage,
            "Grade": grade
        }
    
    print("\n📝 Student Report:")
    for name, info in students.items():
        print(f"{name} - Total Marks: {info['Total Marks']}, Percentage: {info['Percentage']:.2f}%, Grade: {info['Grade']}")

gen_marks()












