# PART 1
# def is_it_okay(current_num, prev_section, after_section, rule_map):
#     for item in prev_section:
#         if item not in rule_map[current_num]["is_after"]:
#             return False
#     for item in after_section:
#         if item not in rule_map[current_num]["is_before"]:
#             return False
#     return True

# with open('input.txt') as file:
#     rules = []
#     sections = []
#     for line in file:
#         if "|" in line:
#             rules.append(line.strip().split("|"))
#         elif "," in line:
#             sections.append(line.strip().split(","))
#     print("rules")
#     print(rules)
#     print("sections")
#     print(sections)
#     ordered_list = []
#     rule_map = {}
#     for rule in rules:
#         a = rule[0]
#         b = rule[1]
#         print("rule",rule)
#         if a not in rule_map:
#             rule_map[a] = {"is_before": [b], "is_after":[]}
#         else:
#             rule_map[a]["is_before"] = rule_map[a]["is_before"]+[b]
#         if b not in rule_map:
#             rule_map[b] = {"is_before": [], "is_after":[a]}
#         else:
#             rule_map[b]["is_after"] = rule_map[b]["is_after"]+[a]
#         print("rule_map", rule_map)
#     print(rule_map)

#     ordered_sections = []
#     for section in sections:
#         print("=========")
#         print(section)
#         yeah_its_good = True
#         for indx in range(len(section)):
#             prev_section = section[0:indx]
#             if indx == 0:
#                 prev_section = []
#             print(section[indx], prev_section, section[indx+1:])
#             if not is_it_okay(section[indx], prev_section, section[indx+1:], rule_map):
#                 yeah_its_good = False
#         if yeah_its_good:
#             ordered_sections.append(section)
#     print(ordered_sections)

#     total = 0
#     for section in ordered_sections:
#         total += int(section[len(section)//2])
#     print(total)


# PART 2
import functools
map_of_map = {}
def compare(item1, item2):
    if item2 in map_of_map[item1]["is_before"]:
        return -1
    if item1 in map_of_map[item2]["is_before"]:
        return 1
    return 0

def is_it_okay(current_num, prev_section, after_section, rule_map):
    for item in prev_section:
        if item not in rule_map[current_num]["is_after"]:
            return False
    for item in after_section:
        if item not in rule_map[current_num]["is_before"]:
            return False
    return True

with open('input.txt') as file:
    rules = []
    sections = []
    for line in file:
        if "|" in line:
            rules.append(line.strip().split("|"))
        elif "," in line:
            sections.append(line.strip().split(","))
    print("rules")
    print(rules)
    print("sections")
    print(sections)
    ordered_list = []
    rule_map = {}
    for rule in rules:
        a = rule[0]
        b = rule[1]
        print("rule",rule)
        if a not in rule_map:
            rule_map[a] = {"is_before": [b], "is_after":[]}
        else:
            rule_map[a]["is_before"] = rule_map[a]["is_before"]+[b]
        if b not in rule_map:
            rule_map[b] = {"is_before": [], "is_after":[a]}
        else:
            rule_map[b]["is_after"] = rule_map[b]["is_after"]+[a]
        print("rule_map", rule_map)
    print(rule_map)
    map_of_map= rule_map

    unordered_sections = []
    for section in sections:
        yeah_its_good = True
        for indx in range(len(section)):
            prev_section = section[0:indx]
            if indx == 0:
                prev_section = []
            if not is_it_okay(section[indx], prev_section, section[indx+1:], rule_map):
                yeah_its_good = False
        if not yeah_its_good:
            unordered_sections.append(section)
    print(unordered_sections)

    total = 0
    for section in unordered_sections:
        print(section)
        section.sort(key=functools.cmp_to_key(compare))
        print(section)
        total += int(section[len(section)//2])
    print(total)

