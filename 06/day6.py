import os



def main():
    in_file = open("06/input.txt", "r")

    all_inputs = []
    for line in in_file:
        all_inputs.append(line.split())

    totals = []
    for col_idx in range(len(all_inputs[0])):
        total = int(all_inputs[0][col_idx])
        for row in all_inputs[1:-1]:
            if all_inputs[-1][col_idx] == '+':
                total += int(row[col_idx])
            elif all_inputs[-1][col_idx] == '*':
                total *= int(row[col_idx])
        totals.append(total)

    all_total = 0
    for total in totals:
        all_total += total

    print(f"sum: {all_total}")


if __name__ == "__main__":
    main()