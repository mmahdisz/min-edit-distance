def minimum_edit_distance(w2, w1):
    arr = [[0 for j in range(len(w1) + 1)] for j in range(len(w2) + 1)]
    steps = [[0 for j in range(len(w1) + 1)] for j in range(len(w2) + 1)]
    for i in range(1, len(w2) + 1):
        arr[i][0] = arr[i - 1][0] + 1
        steps[i][0] = 1
    for i in range(1, len(w1) + 1):
        arr[0][i] = arr[0][i - 1] + 1
        steps[0][i] = 2
    for j in range(1, len(w1) + 1):
        for i in range(1, len(w2) + 1):
            insert = 1 + arr[i - 1][j]
            delete = 1 + arr[i][j - 1]
            if w1[j - 1] == w2[i - 1]:
                add = 0
            else:
                add = 2
            substitute = add + arr[i - 1][j - 1]
            val = min(insert, delete, substitute)
            arr[i][j] = val
            if val == insert:
                steps[i][j] = 1
            elif val == delete:
                steps[i][j] = 2
            else:
                steps[i][j] = 3

    steps_arr = []
    i = len(w2)
    j = len(w1)
    while i > 0 or j > 0:
        if steps[i][j] == 3:
            i -= 1
            j -= 1
            if w1[j] != w2[i]:
                steps_arr.append("substitute " + w1[j] + ", " + w2[i])
        elif steps[i][j] == 2:
            j -= 1
            steps_arr.append("insert " + w1[j])
        elif steps[i][j] == 1:
            i -= 1
            steps_arr.append("delete " + w2[i])
        else:
            print("error")

    for i in range(len(steps_arr) - 1, -1, -1):
        print(steps_arr[i])

    return arr[len(w2)][len(w1)]


w1 = "component"
w2 = "opponent"
print("\nedit distance for", w1, "to", w2, "\ncost:", minimum_edit_distance("iterate", "initial"))
