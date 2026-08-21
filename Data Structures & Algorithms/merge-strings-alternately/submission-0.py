class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        newl = []

        while i < len(word1) and j< len(word2):
            newl.append(word1[i])
            newl.append(word2[j])
            i += 1
            j += 1
        
        if i < len(word1):
            newl += word1[i:]
        
        if j < len(word2):
            newl += word2[j:]

        return "".join(newl)