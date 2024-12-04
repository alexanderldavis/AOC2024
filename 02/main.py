# Part 1

# with open('input.txt') as file:
#     nums = []
#     for line in file:
#         clean_line = line.strip().split()
#         int_list = []
#         for num in clean_line:
#             int_list.append(int(num))
#         nums.append(int_list)
#     safe_lists = 0
#     for line in nums:
#         sorted_list = sorted(line)
#         if sorted_list == line:
#             previous_num = line[0]
#             safe_candidate = True
#             for num in line[1:]:
#                 diff = num - previous_num
#                 previous_num = num
#                 if diff < 1 or diff > 3:
#                     safe_candidate = False
#             if safe_candidate:
#                 safe_lists += 1
#         else:
#             sorted_list = sorted(line, reverse=True)
#             if sorted_list == line:
#                 previous_num = line[0]
#                 safe_candidate = True
#                 for num in line[1:]:
#                     diff = previous_num - num
#                     previous_num = num
#                     if diff < 1 or diff > 3:
#                         safe_candidate = False
#                 if safe_candidate:
#                     safe_lists += 1
#     print(safe_lists)

# Part 2

## Is the list sorted?
### - Check if sorted ASC
### - Check if sorted DESC
### - Else
## IF IT IS:
### - Check if list is safe
### IF IT IS:
### - increase safe list counter
### ELSE:
### - add to bad list



# For every bad list:
# for ever number in the list:
# remove it, and pass that list to the checker func
# if safe, end. else, move to next number

def mega_list_checker(line):
    return is_list_sorted(line) and is_list_safe(sorted(line))


def is_list_sorted(line):
    sorted_list = sorted(line)
    if sorted_list == line:
        return True
    else:
        sorted_list = sorted(line, reverse=True)
        if sorted_list == line:
            return True
        else:
            return False

def is_list_safe(line):
    previous_num = line[0]
    for num in line[1:]:
        diff = num - previous_num
        previous_num = num
        if diff == 0 or diff < 1 or diff > 3:
            return False
    return True

with open('input.txt') as file:
    nums = []
    for line in file:
        clean_line = line.strip().split()
        int_list = []
        for num in clean_line:
            int_list.append(int(num))
        nums.append(int_list)
    safe_lists = 0
    for line in nums:
        if mega_list_checker(line):
            safe_lists+=1
        else:
            for i in range(len(line)):
                newline = line[0:i]+line[i+1:]
                if mega_list_checker(newline):
                    safe_lists+=1
                    break
    print(safe_lists)
