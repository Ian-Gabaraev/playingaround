from typing import List
from copy import deepcopy


class RotatingList:

    def __init__(self, elements: List[int], columns: int):

        if len(elements) != columns ** 2:
            raise ValueError("list must be an even matrix")

        self.elements = elements
        self.length = len(self.elements)
        self.columns = columns

    def rotate_90_deg(self):
        new_list = []
        no_of_slices = [x - 1 for x in range(0, self.columns)]

        for column_number in no_of_slices:

            start = len(self.elements) + (column_number - self.columns + 1)
            end = column_number
            step = -self.columns
            indexes = [x for x in range(start, end, step)]

            for index in indexes:
                new_list.append(self.elements[index])

        self.elements = deepcopy(new_list)

    def rotate_180_deg(self):
        for _ in range(2):
            self.rotate_90_deg()

    def rotate_270_deg(self):
        for _ in range(3):
            self.rotate_90_deg()

    def rotate_360_deg(self):
        pass

    def see(self):
        for sub_range in range(0, self.length, self.columns):
            print(*self.elements[sub_range:sub_range + self.columns])
        print('*' * 5)


if __name__ == '__main__':
    lst_1 = [x for x in range(1, 10)]
    lst_2 = [x for x in range(1, 17)]

    rt_one = RotatingList(elements=lst_1, columns=3)
    rt_two = RotatingList(elements=lst_2, columns=4)

    rt_one.see()
    rt_one.rotate_180_deg()
    rt_one.see()
