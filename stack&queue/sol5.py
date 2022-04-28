"""
문제 : Top K Frequent Elements

요구사항
1. 빈번하게 나온 숫자들 중 k 번까지 출력
"""
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        # value값으로 정렬 후 k 개수만큼 list에 담기
        topk = sorted(counter.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(k):
            result.append(topk[i][0])

        return result


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 5, 5], 2))
