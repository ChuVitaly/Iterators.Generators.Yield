# Task1
"""
Написать итератор, который принимает список списков,
и возвращает их плоское представление,
 т.е последовательность состоящую из вложенных элементов.
"""
# Task1
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
nested_list_all = []
k = 0
while k != len(nested_list):
    for i in nested_list[k]:
        nested_list_all.append(i)
    k += 1




class SampleIterator:

    def __init__(self, nested_list_all):
        self.nested_list_all = nested_list_all
        self.nested_all_len = len(nested_list_all)
        self.n = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.nested_all_len:
            item = self.nested_list_all[self.n]
            self.n += 1
            return item
        raise StopIteration



if __name__ == '__main__':
    for item in SampleIterator(nested_list_all):
        print(item)

    flat_list = [item for item in SampleIterator(nested_list_all)]
    print(flat_list)



# Task2

# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f'],
# 	[1, 2, None],
# ]
#
# result = list()
# for i in (i for lst in nested_list for i in lst):
#     result.append(i)
# print(result)






