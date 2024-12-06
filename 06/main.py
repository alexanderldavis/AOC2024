# PART 1

##0123456789X
#0....#.....
#1.........#
#2..........
#3..#.......
#4.......#..
#5..........
#6.#..^.....
#7........#.
#8#.........
#9......#...
#Y

# def is_hash_safe(map_grid,x,y):
#     try:
#         if map_grid[y][x] == "#":
#             return True
#     except:
#         return False
#     return False

# def can_move_forward(map_grid,coords,direction):
#     x,y = coords
#     if direction == "north" and is_hash_safe(map_grid, x+0, y-1):
#         return False
#     if direction == "east" and is_hash_safe(map_grid, x+1, y+0):
#         return False
#     if direction == "south" and is_hash_safe(map_grid, x+0, y+1):
#         return False
#     if direction == "west" and is_hash_safe(map_grid, x-1, y+0):
#         return False
#     return True

# def get_new_direction(direction):
#     if direction == "north":
#         return "east"
#     if direction == "east":
#         return "south"
#     if direction == "south":
#         return "west"
#     if direction == "west":
#         return "north"

# def move_forard(coords, direction):
#     x,y = coords
#     if direction == "north":
#         return (x+0,y-1)
#     if direction == "east":
#         return (x+1,y+0)
#     if direction == "south":
#         return (x+0,y+1)
#     if direction == "west":
#         return (x-1,y+0)

# def off_the_map(map_grid, coords):
#     x,y=coords
#     if x<0 or y<0 or x>=len(map_grid[0]) or y>=len(map_grid):
#         return True
#     return False

# with open('sample.txt') as file:
#     map_grid = []
#     for line in file:
#         items = []
#         for item in line.strip():
#             items.append(item)
#         map_grid.append(items)
#     print(map_grid)
#     current_coords=()
#     for y in range(len(map_grid)):
#         for x in range(len(map_grid[y])):
#             if map_grid[y][x] == "^":
#                 current_coords=(x,y)
#     print(current_coords)
#     direction="north"
#     set_of_steps = set()
#     while not off_the_map(map_grid, current_coords):
#         set_of_steps.add(current_coords)
#         if can_move_forward(map_grid, current_coords, direction):
#             current_coords = move_forard(current_coords,direction)
#             print(current_coords)
#         else:
#             direction=get_new_direction(direction)
#     print(set_of_steps)
#     print(len(set_of_steps))

# PART 2

##0123456789X
#0....#.....
#1.........#
#2..........
#3..#.......
#4.......#..
#5..........
#6.#..^.....
#7........#.
#8#.........
#9......#...
#Y
import copy
import tqdm
def is_hash_safe(map_grid,x,y):
    try:
        if map_grid[y][x] == "#":
            return True
    except:
        return False
    return False

def can_move_forward(map_grid,coords,direction):
    x,y = coords
    if direction == "north" and is_hash_safe(map_grid, x+0, y-1):
        return False
    if direction == "east" and is_hash_safe(map_grid, x+1, y+0):
        return False
    if direction == "south" and is_hash_safe(map_grid, x+0, y+1):
        return False
    if direction == "west" and is_hash_safe(map_grid, x-1, y+0):
        return False
    return True

def get_new_direction(direction):
    if direction == "north":
        return "east"
    if direction == "east":
        return "south"
    if direction == "south":
        return "west"
    if direction == "west":
        return "north"

def move_forward(coords, direction):
    x,y = coords
    if direction == "north":
        return (x+0,y-1)
    if direction == "east":
        return (x+1,y+0)
    if direction == "south":
        return (x+0,y+1)
    if direction == "west":
        return (x-1,y+0)

def off_the_map(map_grid, coords):
    x,y=coords
    if x<0 or y<0 or x>=len(map_grid[0]) or y>=len(map_grid):
        return True
    return False

with open('input.txt') as file:
    map_grid = []
    for line in file:
        items = []
        for item in line.strip():
            items.append(item)
        map_grid.append(items)
    original_current_coords=()
    for y in range(len(map_grid)):
        for x in range(len(map_grid[y])):
            if map_grid[y][x] == "^":
                original_current_coords=(x,y)
    direction="north"
    set_of_steps = set()
    current_coords = copy.deepcopy(original_current_coords)
    while not off_the_map(map_grid, current_coords):
        set_of_steps.add(current_coords)
        if can_move_forward(map_grid, current_coords, direction):
            current_coords = move_forward(current_coords,direction)
        else:
            direction=get_new_direction(direction)

    num_possible_hinderances = 0
    for possible_coords in tqdm.tqdm(set_of_steps):
        direction = "north"
        current_coords = copy.deepcopy(original_current_coords)
        # print(possible_coords)
        temp_map_grid = copy.deepcopy(map_grid)
        temp_map_grid[possible_coords[1]][possible_coords[0]] = "#"
        # print(temp_map_grid)
        # Caught in a loop:
        # if coords + direction exists in set, it's caught in a loop
        vector_set = set()
        # vector_set = []
        while not off_the_map(temp_map_grid, current_coords) and not (current_coords, direction) in vector_set:
            vector_set.add((current_coords, direction))
            # vector_set.append((current_coords, direction))
            if can_move_forward(temp_map_grid, current_coords, direction):
                current_coords = move_forward(current_coords,direction)
            else:
                direction=get_new_direction(direction)
        # print(current_coords)
        if not off_the_map(temp_map_grid, current_coords):
            num_possible_hinderances+=1
    #     if possible_coords==(3,6):
    #         print(temp_map_grid)
    #         print(vector_set)
    print(num_possible_hinderances)
