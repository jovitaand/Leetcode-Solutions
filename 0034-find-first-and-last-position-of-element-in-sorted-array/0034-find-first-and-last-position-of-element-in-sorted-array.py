class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #https://www.youtube.com/watch?v=4sQL7R5ySUU
        left = self.BinarySearch( nums, target, True) 
        right = self.BinarySearch( nums, target, False)
        return [left,right]
    #we are running the the binary search twice 2*log(n) 
    # leftbias could be true| false if false the result is in the right Bias
    
    def BinarySearch(self, nums, target, LeftBias):
        l, r = 0, len(nums)-1
        i = -1
       
        while l<=r:
            mid = ( l + r ) // 2
            if target > nums[mid]:
                l=mid+1
            elif target< nums[mid]:
                r=mid-1
            else: 
                i = mid #basic binary search
                #we need to keep searching for the target even after finding it as the position of the sorted array is present
                if LeftBias:
                    r = mid -1 #keep searching in the left
                else:
                    l = mid + 1 #keep searching in the right
        return i