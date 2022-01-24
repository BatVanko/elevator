import math

number_of_people = int(input())
capacity = int(input())
result = None
if number_of_people <= capacity:
    result = 1
else:
    result = math.ceil(number_of_people / capacity)
print(result)
