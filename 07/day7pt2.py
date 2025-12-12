import os





def main(filename="input"):
    in_file = open(f"07/{filename}.txt", "r")


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
    timelines = 1
    idx_instances = [0] * len(diagram[0])
    beam_idxs = set()

    for line_idx in range(len(diagram)):
        for char_idx in range(len(diagram[0])):

            if diagram[line_idx][char_idx] == "S":
                idx_instances[char_idx] = 1
                beam_idxs.add(char_idx) 

            if diagram[line_idx][char_idx] == "^":
                if char_idx in beam_idxs:
                    beam_idxs.add(char_idx - 1)
                    beam_idxs.add(char_idx + 1)
                    beam_idxs.remove(char_idx)
                    splits += 1

                    instances = idx_instances[char_idx]
                    idx_instances[char_idx] = 0
                    idx_instances[char_idx - 1] += instances
                    idx_instances[char_idx + 1] += instances
                    timelines += instances


    print(f"Splits: {splits}")
    print(f"Timelines: {timelines}")

if __name__ == "__main__":
    # main("test")
    main()
