import os





def main():
    in_file = open("07/input.txt", "r")


    # Convert input to 2D array
    diagram = []
    row = 0
    for line in in_file:
        diagram.append([])
        for char in line:
            if (char != '\n'):
                diagram[row].append(char)
        row += 1

    splits = 0
    beam_idxs = set()

    for line_idx in range(len(diagram)):
        for char_idx in range(len(diagram[0])):
            if diagram[line_idx][char_idx] == "S":
                beam_idxs.add(char_idx)
            if diagram[line_idx][char_idx] == "^":
                if char_idx in beam_idxs:
                    beam_idxs.add(char_idx - 1)
                    beam_idxs.add(char_idx + 1)
                    beam_idxs.remove(char_idx)
                    splits += 1


    print(f"Splits: {splits}")

if __name__ == "__main__":
    main()