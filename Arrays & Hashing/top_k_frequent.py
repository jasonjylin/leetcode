from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)

        for key, v in counts.items():
            bucket[v].append(key)
        res = []

        for b in reversed(bucket):
            for num in b:
                res.append(num)
                if len(res) == k:
                    return res

        return res
