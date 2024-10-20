class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        for word in words:
            morse = ""
            for char in word:
                morse+=Morse[ord(char)- 97]
            if morse not in res: #to find a unique case
                res.append(morse)
        return (len(res))        
        #https://www.youtube.com/watch?v=fc14ZfL_zNI
            
            