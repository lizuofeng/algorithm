# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/23
"""


# 递归实现
def binary_search_recursion(lst, s, e, aim):
    if s > e or not lst:
        return None
    p = (s + e) // 2
    if lst[p] == aim:
        return p
    elif lst[p] > aim:
        return binary_search_recursion(lst, s, p - 1, aim)
    elif lst[p] < aim:
        return binary_search_recursion(lst, p + 1, e, aim)


# 非递归实现
def binary_search(lst, aim):
    if not lst:
        return None
    s = 0
    e = len(lst) - 1
    while True:
        if s > e:
            return None
        p = (s + e) // 2
        if lst[p] == aim:
            return p
        elif lst[p] > aim:
            e = p - 1
        elif lst[p] < aim:
            s = p + 1


if __name__ == '__main__':
    search_lst = [0, 2, 3, 3.5, 6, 6.3, 10]
    aim_num = 6
    location_recursion = binary_search_recursion(search_lst, 0, len(search_lst) - 1, aim_num)
    location = binary_search(search_lst, aim_num)
    print(location_recursion)
    print(location)
