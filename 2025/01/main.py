dial = 50
zero_count = 0

print(f"{dial=}")

with open("puzzle.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        direction = line[0].capitalize()
        steps = int(line[1:])

        # Move the thing in the appropriate direction
        if direction == "L":
            dial -= steps
        elif direction == "R":
            dial += steps

        # Get appropriate dial
        if dial < 0:
            dial = 100 - (abs(dial) % 100)
        elif dial > 100:
            dial = dial % 100

        # Round up the dial being 100
        if dial == 100:
            dial = 0

        # Add the number of zeros
        if dial == 0:
            zero_count += 1

        if dial == 100:
            print("> ERROR HERE")

        print(f"{direction=}\t\t{steps=}\t\t{dial=}\t\t{zero_count=}")
