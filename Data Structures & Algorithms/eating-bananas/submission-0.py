import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasable(rate):
            min_hours = 0
            for pile in piles : 
                min_hours += math.ceil(pile/rate)
            return min_hours <= h 
        left = 1
        right = max(piles)
        result = -1
        while left <= right : 
            mid = (left+right)//2
            if not feasable(mid):
                left = mid+1
            if feasable(mid):
                right = mid-1
                result = mid
        return result
                