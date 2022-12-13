def change(lst):
    new_start = lst.pop()
    new_end = lst.pop(0)
    lst.append(new_end)
    lst.insert(0, new_start)
    return lst


print(change([1, 2, 3, 4, 5]))
