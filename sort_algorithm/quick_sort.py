# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/24
"""


# 快速排序
def quick_sort(lst, s, e):
    """
    时间复杂度：好:O(nlogn) 均:O(nlogn) 坏:O(n²)
    空间复杂度：O(logn)
    稳定性：不稳定
    """
    if s >= e:
        return
    p = s
    v = lst[s]
    for i in range(s + 1, e + 1):
        if lst[i] < v:
            p += 1
            lst[p], lst[i] = lst[i], lst[p]
    lst[p], lst[s] = lst[s], lst[p]
    quick_sort(lst, s, p - 1)
    quick_sort(lst, p + 1, e)


if __name__ == '__main__':
    sort_lst = [1, 3.5, 4, 0.5, -0.3, 2, 2, 0.5, 1]
    quick_sort(sort_lst, 0, len(sort_lst) - 1)
    print(sort_lst)
