class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left +right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
    #using binary serach to find the first bad version
    #https://www.youtube.com/watch?v=SiDMFIMldgg