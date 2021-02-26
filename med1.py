src = "component"
trg = "opponents"

print("\ncalculaing minimum edit distance for", src, "to", trg, "...\n\n")

src = "#" + src
trg = "#" + trg

# array for numbers of table
edit_table_cost = [[0 for i in range(len(trg))] for j in range(len(src))]
# array for directions of table
edit_table_direction = [["" for i in range(len(trg))] for j in range(len(src))]

# init first row
for i in range(len(trg)):
    edit_table_cost[0][i] = i
    edit_table_direction[0][i] = "←"

# init first column
for i in range(len(src)):
    edit_table_cost[i][0] = i
    edit_table_direction[i][0] = "↑"

# fill first cell with empty
edit_table_direction[0][0] = ""

# fill tables with
for i in range(len(src)):
    for j in range(len(trg)):
        if i == 0 or j == 0:
            continue
        temp_del = edit_table_cost[i - 1][j] + 1
        temp_ins = edit_table_cost[i][j - 1] + 1
        if src[i] == trg[j]:
            temp_sub = edit_table_cost[i - 1][j - 1]
        else:
            temp_sub = edit_table_cost[i - 1][j - 1] + 2

        edit_table_cost[i][j] = min(temp_del, temp_ins, temp_sub)

        if temp_ins == edit_table_cost[i][j]:
            edit_table_direction[i][j] += "←"
        if temp_del == edit_table_cost[i][j]:
            edit_table_direction[i][j] += "↑"
        if temp_sub == edit_table_cost[i][j]:
            edit_table_direction[i][j] += "\\"  # '\' stands for ability to go up-left

# print table of numbers
print("S\\T\t", end='')
for i in range(len(trg)):
    print("\t", trg[i], end='')
print()
for j in range(len(src)):
    print("\t", src[j], end='')
    for i in range(len(trg)):
        print("\t", edit_table_cost[j][i], end='')
    print()

# print table of directions
print()
print("S\\T\t", end='')
for i in range(len(trg)):
    print("\t\t", trg[i], end='')
print()
for j in range(len(src)):
    print("\t", src[j], end='')
    for i in range(len(trg)):
        if len(edit_table_direction[j][i - 1]) == 3 and i - 1 >= 0:  # just making commandline show data clean
            print("\t", edit_table_direction[j][i], end='')
        else:
            print("\t\t", edit_table_direction[j][i], end='')

    print()

# two index to control movement
i = len(src) - 1
j = len(trg) - 1

print()

print("src:\t", src[1:len(src)])
print("trg:\t", trg[1:len(trg)])
print()

med = edit_table_cost[len(src) - 1][len(trg) - 1]

# define two array to save edit data
edit_steps_action = ["" for k in range(med)]
edit_steps_index = [0 for k in range(med)]
edit_steps_argument = ["" for k in range(med)]
index = med - 1

# iterate a path to find one combination of steps
# print("reverse levels:")
while i > 0 or j > 0:
    if edit_table_direction[i][j].__contains__("\\"):
        if src[i] != trg[j]:
            # print("\tsubstitution", src[i], "to", trg[j])
            edit_steps_action[index] = "substitution"
            edit_steps_index[index] = i
            edit_steps_argument[index] = src[i] + trg[j]
            index -= 1
        i -= 1
        j -= 1
    elif edit_table_direction[i][j].__contains__("↑"):
        # print("\tdelete", src[i])
        edit_steps_action[index] = "delete"
        edit_steps_index[index] = i
        edit_steps_argument[index] = src[i]
        index -= 1
        i -= 1
    elif edit_table_direction[i][j].__contains__("←"):
        # print("\tinsert", trg[j])
        edit_steps_action[index] = "insert"
        edit_steps_index[index] = i
        edit_steps_argument[index] = trg[j]
        index -= 1
        j -= 1

# print("\n", edit_steps_action)
# print(edit_steps_index)
# print(edit_steps_argument)

# use steps data to edit src to trg
src_to_trg = src[1:len(src)]
step_index = 0
edit_index = 0
print(src_to_trg)
while step_index < med:
    if edit_steps_action[step_index] == "substitution":
        src_to_trg = \
            src_to_trg[0:edit_steps_index[step_index] + edit_index - 1] + \
            edit_steps_argument[step_index][1] + \
            src_to_trg[edit_steps_index[step_index] + edit_index:len(src_to_trg)]
        print("\t-> substitution", edit_steps_argument[step_index][0], "to", edit_steps_argument[step_index][1])
        print(src_to_trg)
        step_index += 1
        edit_index += 0

    elif edit_steps_action[step_index] == "insert":
        src_to_trg = \
            src_to_trg[0:edit_steps_index[step_index] + edit_index] + \
            edit_steps_argument[step_index] + \
            src_to_trg[edit_steps_index[step_index] + edit_index:len(src_to_trg)]
        print("\t-> insert", edit_steps_argument[step_index])
        print(src_to_trg)
        step_index += 1
        edit_index += 1

    elif edit_steps_action[step_index] == "delete":
        src_to_trg = \
            src_to_trg[0:edit_steps_index[step_index] + edit_index - 1] + \
            src_to_trg[edit_steps_index[step_index] + edit_index:len(src_to_trg)]
        print("\t-> delete", edit_steps_argument[step_index])
        print(src_to_trg)
        step_index += 1
        edit_index -= 1

    else:
        step_index += 1

print("\n\n\tMinimum Edit Distance = ", med)
