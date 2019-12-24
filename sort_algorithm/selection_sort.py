# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/24
"""


# 选择排序
def selection_sort(lst):
    """
    时间复杂度：好:O(n²) 均:O(n²) 坏:O(n²)
    空间复杂度：O(1)
    稳定性：不稳定
    """
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]


if __name__ == '__main__':
    sort_lst = [1, 3.5, 4, 0.5, -0.3, 2, 2, 0.5, 1]
    selection_sort(sort_lst)
    print(sort_lst)
