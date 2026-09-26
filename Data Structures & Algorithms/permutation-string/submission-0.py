from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = Counter(s1)
        window_size = len(s1)
        for i in range(len(s2)-window_size+1):
            if Counter(s2[i:i+window_size]) == target_count:
                return True
        return False
        