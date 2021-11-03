"""
Nasian Ahmed
Coding Question
"""

my_numbers = [5 ,6 ,9, 3, -2, 7, -4, 5]
my_sum = 12
length_array = len(my_numbers)
my_numbers_compare = my_numbers.copy()

def Two_Number_Sum(my_numbers):
    leftIdx = 0
    rightIdx = len(my_numbers) - 1
    result = []
    while leftIdx < rightIdx:
        if my_numbers[leftIdx] + my_numbers[rightIdx] == my_sum:
            result.append(my_numbers[leftIdx]), int(my_numbers[rightIdx])
        else:
             pass
        leftIdx += 1
        rightIdx -= 1
    return result

print(Two_Number_Sum(my_numbers))

