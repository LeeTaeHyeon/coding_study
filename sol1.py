"""
문제 : Implement Stack using Queues

요구사항
1. 두개의 queue를 이용해서 satck을 구현하라 (LIFO)
2. stack의 기능을 구현하기 (push, top, pop, empty)
    2-1 push 요소 추가
    2-2 pop 요소 맨 위의 값을 제거하면서 값을 return
    2-3 top 요소의 맨 위의 값 return
    2-4 empty : 스택이 비어있으면 true, 아니면 false

결과
Runtime: 48 ms, faster than 5.48% of Python online submissions for Implement Stack using Queues.
Memory Usage: 13.7 MB, less than 17.09% of Python online submissions for Implement Stack using Queues.
"""

from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue[:-1]

    def empty(self):
        return len(self.queue) == 0

