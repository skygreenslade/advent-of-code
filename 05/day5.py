import os



def main():
    in_file = open("05/input.txt", "r")

    ranges = []
    fresh = 0

    for line in in_file:
        
        split_line = line.split('-')

        # Ranges are <bottom>-<top> (inclusive)
        if len(split_line) > 1:
            ranges.append(range(int(split_line[0]), int(split_line[1]) + 1))

        # IDs are <num>
        elif len(split_line[0]) > 1:
            is_fresh = False

            # Check if the ID is in any range
            for fresh_range in ranges:
                if int(split_line[0]) in fresh_range:
                    is_fresh = True # keep running because my time is worth more than my PCs

            if is_fresh:
                fresh += 1

        # Blank line - do nothing
        else:
            pass

    print(f"Fresh IDs: {fresh}")






if __name__ == "__main__":
    main()