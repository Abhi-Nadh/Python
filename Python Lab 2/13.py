def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
data=['x','y','z']
print(data)
print(sub_lists(data))

