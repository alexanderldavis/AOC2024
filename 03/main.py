import re

# PART 1
# with open('sample.txt') as file:
#     nums = []
#     sum = 0
#     for line in file:
#         print(line[:-1])
#         pattern = "mul\((\d*)\,(\d*)\)"
#         matches = re.findall(pattern, line)

#         for pair in matches:
#             sum += int(pair[0])*int(pair[1])
#             print(pair)

#         print("---")
#     print(sum)

# PART 2
import time

start = time.perf_counter()
with open('input.txt') as file:
    nums = []
    sum = 0
    do = True
    for line in file:
        # print(line[:-1])
        pattern = "(mul\((\d*)\,(\d*)\)|don't\(\)|do\(\))"
        matches = re.findall(pattern, line)

        for pair in matches:
            if pair[0] == "don't()":
                do = False
            elif pair[0] == "do()":
                do = True
            else:
                if do:
                    sum += int(pair[1])*int(pair[2])
            # print(pair)

        # print("---")
    # print(sum)
end = time.perf_counter()
elapsed = end - start
print(f'Time taken: {elapsed:.6f} seconds')
