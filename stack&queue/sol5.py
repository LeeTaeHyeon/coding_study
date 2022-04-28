"""
문제 : Top K Frequent Elements

요구사항
1. 빈번하게 나온 숫자들 중 k 번까지 출력

결과
Runtime: 95 ms, faster than 68.83% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.8 MB, less than 55.40% of Python online submissions for Top K Frequent Elements.
"""
from collections import defaultdict
from collections import Counter


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


class Solution2(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)

        return [counter.most_common(k)[i][0] for i in range(k)]


sol2 = Solution2()
print(sol2.topKFrequent([1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 5, 5], 2))