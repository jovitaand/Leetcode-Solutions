class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window method
        #https://www.youtube.com/watch?v=wiGpQwVHdE0
        charSet = set()
        left=0
        result=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            result=max(result,right-left+1) #right and left are index values since it is a set it starts from 0 to n
        return result
                
        