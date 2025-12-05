import os
import re



def main():

    in_file = open('02/input1.txt', 'r')
    ranges = in_file.readline().split(',')

    code_sum = 0

    for code_range in ranges:
        ends = code_range.split('-')
        for num in range(int(ends[0]), int(ends[1])+1):
            string_num = str(num)
            dup = re.search("\\b(.+)\\1+\\b", string_num)
            if (dup):
                code_sum += num

    print(code_sum)
    

if __name__ == "__main__":
    main()


