from data import data
from typing import Dict

correct_number = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_ids = set()
power_sets: Dict[str, Dict[str, int]] = dict()
powers = []

for game in data:
    game_id_substring, game_substring = game.split(":")
    _, game_id = game_id_substring.split(" ")
    tries_array = game_substring.split(";")

    minimum_required = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game_ids.add(int(game_id))
    print(game_id)
    for try_substring in tries_array:
        colors_array = try_substring.split(",")


        for color_substring in colors_array:
            color_substring = color_substring.strip()
            color_number, color_name = color_substring.split(" ")
            color_number = int(color_number)
            if (minimum_required[color_name] < color_number):
                minimum_required[color_name] = color_number
            # if (correct_number[color_name] < color_number):
            #     print(game_id, correct_number[color_name], color_number, color_name)
            #     game_ids.discard(int(game_id))

        power_sets[game_id] = minimum_required
# print(game_ids)
# print(sum(game_ids))

# print(power_sets)

for power_set_key, power_set_dict in power_sets.items():
    power = 1

    for color_name, color_number in power_set_dict.items():
        power = power * color_number

    powers.append(power)

total_sum = 0
for power in powers:
    total_sum = total_sum + power
print(powers)
print(total_sum)
