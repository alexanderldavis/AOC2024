# PART 1

# #0 S . . S . . S
# #1 . A . A . A .
# #2 . . M M M . .
# #3 S A M X M A S
# #4 . . M M M . .
# #5 . A . A . A .
# #6 S . . S . . S

# # if -1 -1 = M && -2 -2 = A && -3 -3 = S
# # if +0 -1 = M && +0 -2 = A && +0 -3 = S
# # if +1 -1 = M && +2 -2 = A && +3 -3 = S
# # if -1 +0 = M && -2 +0 = A && -3 +0 = S
# # if +1 +0 = M && +2 +0 = A && +3 +0 = S
# # if -1 +1 = M && -2 +2 = A && -3 +3 = S
# # if +0 +1 = M && +0 +2 = A && +0 +3 = S
# # if +1 +1 = M && +2 +2 = A && +3 +3 = S

# def ie(map_of_maps, coords, letter):
#     try:
#         return map_of_maps[coords[0]][coords[1]] == letter
#     except:
#         return False

# def num_xmases(m, the_x):
#     total = 0
#     print("The x:", the_x)
#     if ie(m, (the_x[0]-1, the_x[1]-1), "M") and ie(m, (the_x[0]-2, the_x[1]-2), "A") and ie(m, (the_x[0]-3, the_x[1]-3), "S"):
#         total += 1
#         print("a")
#     if ie(m, (the_x[0]+0, the_x[1]-1), "M") and ie(m, (the_x[0]+0, the_x[1]-2), "A") and ie(m, (the_x[0]+0, the_x[1]-3), "S"):
#         total += 1
#         print("b")
#     if ie(m, (the_x[0]+1, the_x[1]-1), "M") and ie(m, (the_x[0]+2, the_x[1]-2), "A") and ie(m, (the_x[0]+3, the_x[1]-3), "S"):
#         total += 1
#         print("c")
#     if ie(m, (the_x[0]-1, the_x[1]+0), "M") and ie(m, (the_x[0]-2, the_x[1]+0), "A") and ie(m, (the_x[0]-3, the_x[1]+0), "S"):
#         total += 1
#         print("d")
#     if ie(m, (the_x[0]+1, the_x[1]+0), "M") and ie(m, (the_x[0]+2, the_x[1]+0), "A") and ie(m, (the_x[0]+3, the_x[1]+0), "S"):
#         total += 1
#         print("e")
#     if ie(m, (the_x[0]-1, the_x[1]+1), "M") and ie(m, (the_x[0]-2, the_x[1]+2), "A") and ie(m, (the_x[0]-3, the_x[1]+3), "S"):
#         total += 1
#         print("f")
#     if ie(m, (the_x[0]+0, the_x[1]+1), "M") and ie(m, (the_x[0]+0, the_x[1]+2), "A") and ie(m, (the_x[0]+0, the_x[1]+3), "S"):
#         total += 1
#         print("g")
#     if ie(m, (the_x[0]+1, the_x[1]+1), "M") and ie(m, (the_x[0]+2, the_x[1]+2), "A") and ie(m, (the_x[0]+3, the_x[1]+3), "S"):
#         total += 1
#         print("h")
#     return total

# with open('input.txt') as file:
#     nums = []
#     sum = 0
#     map_of_maps = {}
#     i = 0
#     for line in file:
#         line_letters = {}
#         for letter in range(len(line.strip())):
#             line_letters[letter] = line[letter]
#         map_of_maps[i] = line_letters
#         i+=1
#     xmas_count = 0
#     for line_i in range(len(map_of_maps)):
#         line = map_of_maps[line_i]
#         for letter in range(len(line)):
#             if line[letter] == "X":
#                 xmas_count += num_xmases(map_of_maps, (line_i, letter))
#     print(xmas_count)

# PART 2

# M.M
# .A.
# S.S

# S.M
# .A.
# S.M

# S.S
# .A.
# M.M

# M.S
# .A.
# M.S

# if -1 -1 == "M" && +1 -1 == "M" && -1 +1 == "S" && +1 +1 == "S"
# if -1 -1 == "S" && +1 -1 == "M" && -1 +1 == "S" && +1 +1 == "M"
# if -1 -1 == "S" && +1 -1 == "S" && -1 +1 == "M" && +1 +1 == "M"
# if -1 -1 == "M" && +1 -1 == "S" && -1 +1 == "M" && +1 +1 == "S"

def ie(map_of_maps, coords, letter):
    try:
        return map_of_maps[coords[0]][coords[1]] == letter
    except:
        return False

def is_an_x(m, the_a):
    print("The a:", the_a)
    if ie(m, (the_a[0]-1, the_a[1]-1), "M") and ie(m, (the_a[0]+1, the_a[1]-1), "M") and ie(m, (the_a[0]-1, the_a[1]+1), "S") and ie(m, (the_a[0]+1, the_a[1]+1), "S"):
        return True
    if ie(m, (the_a[0]-1, the_a[1]-1), "S") and ie(m, (the_a[0]+1, the_a[1]-1), "M") and ie(m, (the_a[0]-1, the_a[1]+1), "S") and ie(m, (the_a[0]+1, the_a[1]+1), "M"):
        return True
    if ie(m, (the_a[0]-1, the_a[1]-1), "S") and ie(m, (the_a[0]+1, the_a[1]-1), "S") and ie(m, (the_a[0]-1, the_a[1]+1), "M") and ie(m, (the_a[0]+1, the_a[1]+1), "M"):
        return True
    if ie(m, (the_a[0]-1, the_a[1]-1), "M") and ie(m, (the_a[0]+1, the_a[1]-1), "S") and ie(m, (the_a[0]-1, the_a[1]+1), "M") and ie(m, (the_a[0]+1, the_a[1]+1), "S"):
        return True
    return False

with open('input.txt') as file:
    nums = []
    sum = 0
    map_of_maps = {}
    i = 0
    for line in file:
        line_letters = {}
        for letter in range(len(line.strip())):
            line_letters[letter] = line[letter]
        map_of_maps[i] = line_letters
        i+=1
    xmas_count = 0
    for line_i in range(len(map_of_maps)):
        line = map_of_maps[line_i]
        for letter in range(len(line)):
            if line[letter] == "A":
                if is_an_x(map_of_maps, (line_i, letter)):
                    xmas_count += 1
    print(xmas_count)
