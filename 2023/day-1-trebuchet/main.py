from data import data
import re

# Part 1
numbers_in_data = []
for word in data:
    numbers_in_word = []
    for letter in word:
        try:
            number = int(letter)
            numbers_in_word.append(number)
        except Exception:
            pass
    final_number = numbers_in_word[0] * 10 + numbers_in_word[-1]
    # print(str(final_number))
    numbers_in_data.append(final_number)

total_sum = 0

for number in numbers_in_data:
    total_sum = total_sum + number

print(total_sum)

# Part 2
numbers_as_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_as_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_as_strings_and_digits = numbers_as_strings + numbers_as_digits

numbers_in_data_2 = []

for word in data:
    matches_in_word = []

    # Extract where numbers occur and their indexes
    for number_as_string_or_digit in numbers_as_strings_and_digits:
        for match in re.finditer(number_as_string_or_digit, word):
            matches_in_word.append((match.start(), number_as_string_or_digit))

    # Get max and min element
    # i take the last element at the end there viamindexing
    first_number = min(matches_in_word, key=lambda x: x[0])[1]
    last_number = max(matches_in_word, key=lambda x: x[0])[1]

    final_number = 0
    # Do appropriate conversion for first and last number
    try:
        number = int(first_number)
        print('number',number)
        final_number = final_number + (number * 10)
    except Exception:
        number_to_add = 0
        if first_number == "one":
            number_to_add = 1
        elif first_number == "two":
            number_to_add = 2
        elif first_number == "three":
            number_to_add = 3
        elif first_number == "four":
            number_to_add = 4
        elif first_number == "five":
            number_to_add = 5
        elif first_number == "six":
            number_to_add = 6
        elif first_number == "seven":
            number_to_add = 7
        elif first_number == "eight":
            number_to_add = 8
        elif first_number == "nine":
            number_to_add = 9

        final_number = final_number + (number_to_add * 10)

    try:
        number = int(last_number)
        final_number = final_number + number
    except Exception:
        number_to_add = 0
        if last_number == "one":
            number_to_add = 1
        elif last_number == "two":
            number_to_add = 2
        elif last_number == "three":
            number_to_add = 3
        elif last_number == "four":
            number_to_add = 4
        elif last_number == "five":
            number_to_add = 5
        elif last_number == "six":
            number_to_add = 6
        elif last_number == "seven":
            number_to_add = 7
        elif last_number == "eight":
            number_to_add = 8
        elif last_number == "nine":
            number_to_add = 9

        final_number = final_number + number_to_add

    numbers_in_data_2.append(final_number)

    print(matches_in_word, first_number, last_number, final_number)

total_sum_2 = 0

for num in numbers_in_data_2:
    total_sum_2 = total_sum_2 + num

print("Total Sum 2:", total_sum_2)
