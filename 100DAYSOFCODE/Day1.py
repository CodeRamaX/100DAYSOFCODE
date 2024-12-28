numbers = [1,2,3,4,5,6,7,8,9,10]

even_num = [num for num in numbers if num % 2 == 0]

print("Even numbers:", even_num)

squares_div_by_3 = [i**2 for i in range(1, 11) if i % 3 == 0]

print("Squares of numbers divisible by 3:", squares_div_by_3)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print("3x3 Matrix")
for row in matrix:
    print(row)
original_dict = {"a": 1, "b": 2, "c": 3}

modified_dict = {key.upper(): value * 10 for key, value in original_dict.items()}

print("Modified dictionary:", modified_dict)

















