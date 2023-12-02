from data import data

correct_number = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_ids = set()

for game in data:
    game_id_substring, game_substring = game.split(":")
    _, game_id = game_id_substring.split(" ")
    tries_array = game_substring.split(";")

    game_ids.add(int(game_id))
    print(game_id)
    for try_substring in tries_array:
        colors_array = try_substring.split(",")

        for color_substring in colors_array:
            color_substring = color_substring.strip()
            color_number, color_name = color_substring.split(" ")
            color_number = int(color_number)
            if (correct_number[color_name] < color_number):
                print(game_id, correct_number[color_name], color_number, color_name)
                game_ids.discard(int(game_id))

print(game_ids)
print(sum(game_ids))
