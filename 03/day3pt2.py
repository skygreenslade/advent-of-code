import os
from textwrap import wrap




def main():

    in_file = open("03/input1.txt", 'r')

    total_joltage = 0

    for line in in_file:
        values = wrap(line,1)
        joltage_values = [0]
        joltage_indexes = [-1]

        values.append('0')

        num_batteries = 12
        for battery in range(num_batteries):
            
            batteries_to_select = num_batteries - battery
            starting_index = joltage_indexes[-1] + 1
            slice_to_check = values[starting_index:-batteries_to_select]

            # Get highest value exluding last n values
            joltage_values.append(max(slice_to_check))

            joltage_indexes.append(slice_to_check.index(joltage_values[-1]) + starting_index)
            

        # Calculate Joltage
        joltage = "".join(map(str,joltage_values))

        # Add to total
        total_joltage += int(joltage)
    

    print(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    main()