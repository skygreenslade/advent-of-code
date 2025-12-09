import os



def main():
    in_file = open("05/input.txt", "r")

    ranges = []
    fresh = 0
    line_num = 0

    start = [0,0]
    ranges = [start]

    for line in in_file:
        line_num += 1    
        split_line = line.split('-')

        # Ranges are <bottom>-<top> (inclusive)
        if len(split_line) > 1:
            
            new_low = int(split_line[0])
            new_high = int(split_line[1])
            
            idx = 0
            while idx < len(ranges) and new_low > ranges[idx][0]:
                idx+=1
            
            # Sort ranges by minimum
            ranges.insert(idx, [new_low, new_high])
            
        # Do not care about blank line or IDs
        else:
            pass


    # Consolidate overlapping ranges
    consolidated = []
    low_idx = 0
    high_idx = 0
    while (high_idx < len(ranges)):
        low = ranges[low_idx][0]
        high = ranges[high_idx][1]
        incremented = True

        while incremented:
            incremented = False
            while low_idx < (len(ranges)) and high >= ranges[low_idx][0]:
                low_idx += 1
                high = max(high, ranges[low_idx - 1][1])
                incremented = True

        consolidated.append([low, high])
        high_idx = low_idx

    # calculate number of fresh IDs
    for low, high in consolidated[1:]:
        fresh += 1 + high - low

# Too low : 304540402086486
            
    print(f"fresh IDs: {fresh}")






if __name__ == "__main__":
    main()