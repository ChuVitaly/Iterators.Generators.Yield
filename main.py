
# Task1
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Вариант 1
# k = 0
# while k != len(nested_list):
#     s = 0
#     a = (x for x in nested_list[k])
#     while s != len(nested_list[k]):
#         print(next(a))
#         s += 1
#     k += 1


# Вариант 2
for i in (i for lst in nested_list for i in lst):
    print(i)






