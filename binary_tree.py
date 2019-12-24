# -*- encoding: utf-8 -*-
"""
    :author: zfli
    :date: 2019/12/23
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        if self.root is None:
            return
        stack = list()
        node = self.root
        while node or stack:
            while node:
                print(node.data, end=' ')
                stack.append(node)
                node = node.left

            node = stack.pop()
            node = node.right
        print()

    def mid_order(self):
        if self.root is None:
            return
        stack = list()
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.data, end=' ')
            node = node.right
        print()

    def post_order(self):
        if self.root is None:
            return
        stack1 = list()
        stack2 = list()
        stack1.append(self.root)
        while stack1:
            node = stack1.pop()
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().data, end=' ')
        print()

    def level_order(self):
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        queue.append('next')
        while queue:
            node = queue.pop(0)
            if node == 'next':
                print()
                if queue:
                    queue.append('next')
                continue
            print(node.data, end=' ')

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()


if __name__ == '__main__':
    root_node = Node(1, Node(2, Node(4), Node(5, Node(8))), Node(3, Node(6), Node(7, Node(9))))
    tree = Tree(root_node)
    print('pre order:')
    tree.pre_order()
    print('mid order:')
    tree.mid_order()
    print('post order:')
    tree.post_order()
    print('level order:')
    tree.level_order()
