# Task1
"""
Написать итератор, который принимает список списков,
и возвращает их плоское представление,
 т.е последовательность состоящую из вложенных элементов.
"""
# Task1
# Вариант 1
# nested_list = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None],
# ]
# nested_list_all = []
# k = 0
# while k != len(nested_list):
#     for i in nested_list[k]:
#         nested_list_all.append(i)
#     k += 1
#
#
#
#
# class SampleIterator:
#
#     def __init__(self, nested_list_all):
#         self.nested_list_all = nested_list_all
#         self.nested_all_len = len(nested_list_all)
#         self.n = 0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.nested_all_len:
#             item = self.nested_list_all[self.n]
#             self.n += 1
#             return item
#         raise StopIteration
#
#
#
# if __name__ == '__main__':
#     for item in SampleIterator(nested_list_all):
#         print(item)
#
#     flat_list = [item for item in SampleIterator(nested_list_all)]
#     print(flat_list)

# Task1
# Вариант 2

class SampleIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.nested_list_all = []

    def __iter__(self):
        self.nested_list_cursor = 0
        self.nested_list_all_cursor = -1
        return self

    def __next__(self):
        while self.nested_list_cursor != len(self.nested_list):
            for i in self.nested_list[self.nested_list_cursor]:
                self.nested_list_all.append(i)
            self.nested_list_cursor += 1
        if self.nested_list_cursor <= len(self.nested_list):
            for i in self.nested_list:
                self.nested_list_all.extend(i)
            self.nested_list_cursor += 1
        if self.nested_list_all_cursor + 1 >= len(self.nested_list_all):
            raise StopIteration()
        self.nested_list_all_cursor += 1
        return self.nested_list_all[self.nested_list_all_cursor]

        

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    a = SampleIterator(nested_list)
    print(a)
    for k in a:
        print(k)


    # --------------------- Проверка ---------------------------------

    # expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    #
    # i = 0
    #
    # for item in SampleIterator(nested_list):
    #     print('item == expected_result[i]', item == expected_result[i])
    #     i += 1



# Task2
"""
Написать генератор, который принимает список списков, и возвращает их плоское представление
"""

# nested_list = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     [1, 2, None],
# ]
#
# def get_list(nested_list):
#     for item in (item for lst in nested_list for item in lst):
#         yield item
#
#
# a = get_list(nested_list)
# print(a)
# print(list(a))
# for x in a:
#     print(x)
