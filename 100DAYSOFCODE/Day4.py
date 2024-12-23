def class_report(data):
    total_students = len(data)
    total_grades = sum(data.values())
    average_grade = total_grades / total_students
    print(" "*10)
    report = "🗒️  Student Grades Report\n"
    report += "-" * 25 + "\n"
    for name, grade in data.items():
        report += f"🎓 {name}: {grade}\n"
    report += "-" * 25 + "\n"
    report += f"Total Students: {total_students}\n"
    report += f"Average Grade: {average_grade:.2f}\n"
    report += f"Highest Grade: {max(data.values())} (By {max(data, key=data.get)})\n"
    report += f"Lowest Grade: {min(data.values())} (By {min(data, key=data.get)})\n"
    return report
data = {"Prateek": 85,"Dhruv": 92,"Ramesh": 78,"Sameer": 90,"Payal": 88}
print(class_report(data))

def shopping_cart(*args, **kwargs):
    total_cost = sum(item[1] for item in args)
    discount = kwargs.get('discount', 0)
    if discount > 0:
        total_cost -= total_cost * (discount / 100)
    tax = kwargs.get('tax', 0)
    if tax > 0:
        total_cost += total_cost * (tax / 100)
    return round(total_cost, 2)
items = [("Orange", 30), ("Banana", 10), ("Milk", 50), ("Bread", 40)]
final_cost = shopping_cart(*items, discount=10, tax=5)
print("Final Cost of Shopping Cart:", "₹",final_cost)












