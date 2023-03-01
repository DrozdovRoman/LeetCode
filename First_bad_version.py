# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        good, bad = 0, n
        while (bad > good + 1):
            mid = good + ((bad - good) // 2)
            if isBadVersion(mid):
                bad = mid
            else:
                good = mid
        return bad