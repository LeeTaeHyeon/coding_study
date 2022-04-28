"""
문제 : Implement Queue using Stacks

요구사항
1. 두개의 stack을 이용해서 queue를 구현하라 (FIFO)
2. queue의 기능을 구현하기 (push, pop, peek, empty)
    2-1 push 요소 추가
    2-2 pop 제일 먼저 추가된 요소 값을 제거하면서 값을 return
    2-3 peek 제일 먼저 추가된 요소 값 return
    2-4 empty : 스택이 비어있으면 true, 아니면 false

결과
Runtime: 20 ms, faster than 64.86% of Python online submissions for Implement Queue using Stacks.
Memory Usage: 13.7 MB, less than 14.18% of Python online submissions for Implement Queue using Stacks.
"""
from collections import deque


class MyQueue(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.popleft()

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0
