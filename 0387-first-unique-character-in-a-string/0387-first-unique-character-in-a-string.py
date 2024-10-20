class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s) 
        for indx, ch in enumerate(s):
            if count[ch] ==1:
                return indx
        return -1
    #build a hashmap 
    #iterate and check if the character is in the hashmap
    '''
    collection is an inbuilt funtion that is used as a container to store values like
    tuple, list, set, dict etc.
    Counter function used in conjunction with collection
    enumerate() only accepts collection as a input
    
    '''