
# PART 1
# with open('sample.txt') as file:
#     l_nums = []
#     r_nums = []
#     for line in file:
#         clean_line = line.strip()
#         nums = clean_line.split()
#         l_nums.append(int(nums[0]))
#         r_nums.append(int(nums[1]))
#     print(l_nums)
#     l_nums.sort()
#     r_nums.sort()
#     print(len(l_nums))
#     print(len(r_nums))
#     sum_of_differences = 0
#     for i in range(len(l_nums)):
#         l_num = l_nums[i]
#         r_num = r_nums[i]
#         difference = 0
#         if l_num < r_num:
#             difference = r_num-l_num
#         else:
#             difference = l_num-r_num
#         sum_of_differences += difference
#     print(sum_of_differences)

# PART 2
with open('input.txt') as file:
    l_nums = []
    r_nums = {}
    for line in file:
        clean_line = line.strip()
        nums = clean_line.split()
        l_nums.append(int(nums[0]))
        r_num = int(nums[1])
        if r_num not in r_nums:
            r_nums[r_num] = 0
        r_nums[r_num] = r_nums[r_num] + 1
    sim_score = 0
    for num in l_nums:
        if num in r_nums:
            sim_score += num * r_nums[num]
    print(sim_score)