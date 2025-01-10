import pandas as pd
data = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
           111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'Name': ['Aarav Sharma', 'Vihaan Mehta', 'Ananya Gupta', 'Ishaan Patel', 'Diya Kapoor', 'Riya Singh',
             'Aditya Verma', 'Nisha Chawla', 'Karan Desai', 'Arjun Malhotra',
             'Meera Joshi', 'Kabir Khanna', 'Aditi Rao', 'Yash Agrawal', 'Sakshi Bansal', 'Tanishq Chauhan',
             'Kriti Nair', 'Aman Tiwari', 'Sneha Ghosh', 'Raghav Mishra'],
    'Marks': [85, 78, 92, 34, 67, 45, 39, 56, 88, 73, 49, 64, 31, 79, 81, 58, 60, 25, 72, 41]
}

df = pd.DataFrame(data)
passed_students = df.loc[df['Marks'] >= 50]
sorted_passed_students = passed_students.sort_values(by='Marks', ascending=False)
print("Students who passed, sorted by marks:")
print(sorted_passed_students)
sorted_passed_students.to_csv('passed_students.csv', index=False)
print("\nData has been saved to 'passed_students.csv'")



