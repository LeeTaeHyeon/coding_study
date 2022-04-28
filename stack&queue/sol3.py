"""
문제 : Find the Winner of the Circular Game

요구사항
1. n명의 플레이어, 1번부터 n번까지 시계방향으로 의자에 앉아있다.
2. 1번을 포함해 시계방향으로 돌다가, k 번째 플레이어를 아웃
3. 1명 이상 플레이어가 있으면, 아웃된 플레이어 다음번부터 2번을 반복

결과
Runtime: 30 ms, faster than 70.41% of Python online submissions for Find the Winner of the Circular Game.
Memory Usage: 13.4 MB, less than 69.82% of Python online submissions for Find the Winner of the Circular Game.
"""

"""
ex 1) k = 2
1 2 3 4 5 / out index 1 (0 + k - 1)
1 3 4 5 / out index 2 (1 + k - 1)
1 3 5 / out index 0 (2 + k - 1) -> index 넘어가면 나머지 연산
3 5 / out index 1  (0 + k -1)
"""
from collections import deque


class Solution(object):
    def __init__(self):
        self.queue = deque()

    def findTheWinner(self, n, k):
        self.queue = [i for i in range(1, n + 1)]
        index = 0
        while not len(self.queue) == 1:
            if index + k - 1 >= len(self.queue):
                index = (index + k - 1) % len(self.queue)
            else:
                index = index + k - 1

            self.queue.pop(index)

        return self.queue.pop()


sol = Solution()
print(sol.findTheWinner(5, 2))


