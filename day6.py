
#----------------------------------------
# Part 1
# import day6_input.txt as a list of sets
s = set()
set_list = [];
sum_counts = 0;
with open("day6_input.txt") as f:
    for line in f:
        if len(line.strip('\n')) != 0:
             set_line = set(line.rstrip('\n'))
             s={*s, *set_line}
        else:
             set_list.append(s)
             sum_counts += len(s)
             s = set()
# Add the last set crreated if the last line of the file is not blank
if len(line.strip('\n')) != 0:
    set_list.append(s)
    sum_counts += len(s)
    s = set()

#----------------------------------------
# Part 2
# import day6_input.txt as a list of sets
list_lines = []
set_list = [];
sum_counts = 0;
with open("day6_input.txt") as f:
    for line in f:
        if len(line.strip('\n')) != 0:
             list_lines.append(set(line.rstrip('\n')))
        else:
             s =list_lines[0].intersection(*list_lines) # intersect list of set
             set_list.append(s)
             sum_counts += len(s)
             list_lines = []
# Add the last set crreated if the last line of the file is not blank
if len(line.strip('\n')) != 0:
             s =list_lines[0].intersection(*list_lines)
             set_list.append(s)
             sum_counts += len(s)
             list_lines = []
