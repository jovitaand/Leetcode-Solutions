class Solution(object):
    def countBinarySubstrings(self, s):
        q= deque() #doubly ended queue
        count=0
        for char in s:
            while q and q[-1]==char and q[0]!=char:
                q.pop()
            if q and q[-1]!=char:
                q.pop()
                count+=1
            q.appendleft(char) #appends the element in the left side of the queue
        return count
    #https://www.youtube.com/watch?v=7tJlUfArIE8e
    
    #since we need the elements to be consecutive we are popping the elements that are equal to the end but not the beginning much like a sliding window
                
        