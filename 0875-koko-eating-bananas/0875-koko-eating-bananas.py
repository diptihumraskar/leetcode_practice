class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            k = (lo + hi) // 2
            hours = sum((p + k - 1) // k for p in piles)  # ceil(p / k)
            if hours <= h:
                hi = k          # k works; look for something smaller
            else:
                lo = k + 1      # k too slow
        return lo