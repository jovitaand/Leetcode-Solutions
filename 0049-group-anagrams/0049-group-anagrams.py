class Solution(object):
    def groupAnagrams(self, strs):
        anagramMap = defaultdict(list)
        for word in strs:
            anagramMap[''.join(sorted(word))].append(word)
            
        return anagramMap.values()