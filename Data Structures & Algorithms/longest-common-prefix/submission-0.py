class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp=""
        for i in range(len(strs[0])):
            st = strs[0][i]
            
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or st != strs[j][i]:
                    return lcp
            
            lcp += st
            
            
        return lcp
