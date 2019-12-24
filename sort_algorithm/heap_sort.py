# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/24
"""
from collections import deque
"""
参考：https://www.jianshu.com/p/d174f1862601
两个难点：1.如何把一个序列构造出一个大根堆
         2.输出堆顶元素后，如何使剩下的元素构造出一个大根堆
"""


def swap_param(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def heap_adjust(lst, s, e):
    # temp为根节点的值
    temp = lst[s]

    # i为根节点坐标
    i = s
    # j为左节点坐标
    j = 2 * i

    # 保证遍历完整棵树
    while j <= e:
        # 保证j取到较大子树坐标
        if j < e and lst[j] < lst[j + 1]:
            j += 1

        # 如果根节点小于子树节点则进行兑换（构建大根堆）
        if temp < lst[j]:
            lst[i] = lst[j]
            i = j
            j = 2 * i
        else:
            break
    lst[i] = temp


def heap_sort(lst):
    l_length = len(lst) - 1

    # 因为满节点与叶子节点的关系为n = N + 1，所以一共有2N + 1个节点，即l_length,
    # 可求满节点数及小子数的个数N为l_length // 2
    first_sort_count = l_length // 2
    for i in range(first_sort_count):
        heap_adjust(lst, first_sort_count - i, l_length)

    for i in range(l_length - 1):
        swap_param(lst, 1, l_length - i)
        heap_adjust(lst, 1, l_length - i - 1)

    return [lst[i] for i in range(1, len(lst))]


if __name__ == '__main__':
    # 使用deque原因是内部为链表结构，在最左侧插入时间复杂度为O(1), list的insert在最左侧插入的时间复杂度为O(n)
    L = deque([1, 3.5, 4, 0.5, -0.3, 2, 2, 1])
    L.appendleft(0)
    result_lst = heap_sort(L)
    print(result_lst)
