set_maths = {"Rajeev", "Bhavya", "Charan", "Daksh", "Chris","Varun"}
set_Computer = {"Charan", "Chris", "Frank", "Rajeev", "Bhavya","Harish"}
# Students enrolled in at least one course (Union)
atleastone_course = set_maths.union(set_Computer)
print("Students in at least one course:", atleastone_course)
# Students in both courses(Intersection)
Bothcourses_set = set_maths.intersection(set_Computer)
print("Students in both courses:", Bothcourses_set)
# Students in only one course(Symmetric Difference)
onlyone_course = set_maths.symmetric_difference(set_Computer)
print("Students in only one course:",onlyone_course)
# Check if all CS students are in Mathematics
computer_in_math = set_Computer.issubset(set_maths)
print("Are all CS students also in Mathematics?:", computer_in_math)

# PYTHON BUILT IN FUNCTIONS

#use abs() to find the absolute value of a given number
print(abs(-19))
# use chr() function to find the characters corresponding to the given Unicode
num = [95, 74, 36, 61]
for i in num:
  print(chr(i))
# Using Dict() and zip() for converting given data of keys and values as list into a dictionary 
value=["One","Two","Three","Four","Five"]
keys=[1,2,3,4,5]
dict_main=dict(zip(value,keys))
print(dict_main)
#  Using enumerate() to provide the index value of each items
car_list = ["Honda","Tata","Mahindra","Toyota","Hyundai"]
e_car_list  = enumerate(car_list)
print(list(e_car_list))





