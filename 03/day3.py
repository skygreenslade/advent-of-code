import os
from textwrap import wrap




def main():

    in_file = open("03/input1.txt", 'r')

    total_joltage = 0

    for line in in_file:
        values = wrap(line,1)

        # Get highest value before last index
        highest = max(values[:-1])

        # Get highest value after highest index
        next_highest = max(values[values.index(highest)+1:])

        # Calculate Joltage
        max_joltage = int(highest)*10 + int(next_highest)

        # Add to total
        total_joltage += max_joltage
    

    print(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    main()