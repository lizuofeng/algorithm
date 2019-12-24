# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/24
"""


# 冒泡排序
def bubble_sort(lst):
    """
    时间复杂度：好:O(n) 均:O(n²) 坏:O(n²)
    空间复杂度：O(1)
    稳定性：稳定
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]


if __name__ == '__main__':
    sort_lst = [1, 3.5, 4, 0.5, -0.3, 2, 2, 0.5, 1]
    bubble_sort(sort_lst)
    print(sort_lst)
