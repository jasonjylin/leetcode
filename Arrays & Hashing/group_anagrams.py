from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                char_code = ord(c) - ord("a")
                key[char_code] += 1

            d[tuple(key)].append(s)

        return d.values()
