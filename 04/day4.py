import os
from textwrap import wrap





def main():
    in_file = open("04/input.txt", "r")

    # Create 2D array of wall
    wall = []
    for line in in_file:
        wall.append(wrap(line,1))

    total_rolls = 0
    rolls = 1
    while rolls > 0:
        rolls = get_all_rolls(wall)
        total_rolls += rolls


    print(f"Gettable rolls: {total_rolls}")


def num_adjacent_rolls(wall, row, col):
    num_adjacent_rolls = -1
    start_row = max(row-1, 0)
    end_row = min(row+2, len(wall))
    start_col = max(col-1, 0)
    end_col = min(col+2, len(wall[row]))

    rows = range(start_row, end_row)
    cols = range(start_col, end_col)
    for row_num in rows:
        for col_num in cols:
            if wall[row_num][col_num] == '@':
                num_adjacent_rolls +=1 

    return num_adjacent_rolls


def get_all_rolls(wall):
    rolls = 0
    for row_num in range(len(wall)):
        for col_num in range(len(wall[row_num])):
            # Check if a roll exists there
            if wall[row_num][col_num] == '@':
                if num_adjacent_rolls(wall, row_num, col_num) < 4:
                    rolls+=1
                    wall[row_num][col_num] = '.'
    
    return rolls

if __name__ == "__main__":
    main()