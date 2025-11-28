# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = tuple(s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')
            groups[key].append(s)
        return list(groups.values())
