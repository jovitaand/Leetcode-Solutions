class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for words in sentences:
            word=words.split()
            res=max(res,len(word))
        return res
            