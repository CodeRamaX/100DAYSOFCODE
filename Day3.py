def categorize_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers
numbers = [10, 15, 22, 33, 40, 55, 60]
even, odd = categorize_numbers(numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

def longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    max_len = 0
    for word in words:
        if len(word) > max_len:
            longest_word = word
            max_len = len(word)
    return longest_word, max_len
sentence = "The future belongs to those who believe in the beauty of their dreams"
longest_word, length = longest_word(sentence)
print("Longest word:", longest_word)
print("Length:", length)

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)
num_in=int(input("Enter the Number: "))
print(harmonic_sum(num_in))

def LCM(x, y):  
  z = x % y  
  if z == 0:  
        return x  
  return x * LCM(y, z) / z  
print("The least common factor is: ", LCM(8, 9))  
