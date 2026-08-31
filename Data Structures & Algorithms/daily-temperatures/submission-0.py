class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        
        st = [] #stores in [temp,index]

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                st_t, st_i = st.pop()
                res[st_i] = i - st_i
            st.append([t,i])
        
        return res