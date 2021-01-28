#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        ans = []
        if not root:
            return ans

        q = deque()
        q.append((0, root))
        while q:
            (depth, t) = q.popleft()
            if len(ans) <= depth:
                ans.append([])
            ans[depth].append(t.val)
            for c in (t.left, t.right):
                if c:
                    q.append((depth + 1, c))

        for i in range(len(ans)):
            if i % 2:
                ans[i] = ans[i][::-1]
        return ans
