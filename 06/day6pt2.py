import os
import numpy as np


def main():
    in_file = open("06/input.txt", "r")

    # convert input into array
    all_inputs = []
    for line in in_file:
        char_arr = []
        for char in line:
            if char != '\n':
                char_arr.append(char)
        all_inputs.append(char_arr)


    # rotate array (as np)
    while len(all_inputs[-1]) < len(all_inputs[0]):
        all_inputs[-1].append(' ')
    rotated = np.array(all_inputs)
    rotated = np.rot90(rotated)
    print(rotated)

    totals = []
    values = []
    last_value = False
    skip = False
    for row in rotated:
        if row[-1] == '+' or row[-1] == '*':
            last_value = True

        value = 0
        base = 1
        # get number
        for char in reversed(row[:-1]):
            if char != ' ':
                value += int(char) * base
                base *= 10

        # Add number to list
        if skip:
            skip = False
        else:
            values.append(value)


        if last_value:
            last_value = False
            skip = True

            total = values[0]
            for value in values[1:]:
                if row[-1] == '+':
                    total += value
                elif row[-1] == '*':
                    total *= value

            totals.append(total)

            # Reset array
            values = []

    grand_total = 0
    for total in totals:
        grand_total += total

    print(f"grand total: {grand_total}")


if __name__ == "__main__":
    main()