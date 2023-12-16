import numpy as np


text_file = open(file="day1_input.txt").read()

numbers = []

first_number = None
second_number = None

for symbol in text_file:
    if symbol.isdigit() and (first_number is None):
        first_number = symbol
    elif symbol.isdigit():
        second_number = symbol
    elif symbol == "\n":
        if first_number is not None and second_number is not None:
            numbers.append(int(str(first_number) + str(second_number)))
        elif second_number is None:
            numbers.append(int(str(first_number) + str(first_number)))

        first_number = None
        second_number = None

if first_number is not None and second_number is not None:
    numbers.append(int(str(first_number) + str(second_number)))
elif second_number is None:
    numbers.append(int(str(first_number) + str(first_number)))


list_sum = 0
for i in range(len(numbers)):
    print(numbers[i])
    list_sum = list_sum + numbers[i]

