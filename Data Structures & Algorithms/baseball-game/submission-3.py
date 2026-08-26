class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        st = []
        for i in operations:
                
            if i == "+":
                st.append(st[-1] + st[-2])
                score += st[-1]
                
            elif i == "D":
                st.append(st[-1]*2)
                print(st)
                score += st[-1]
                
                
            elif i == "C":
                score -= st.pop()
            else :
                st.append(int(i))
                score += st[-1]
                               

        return score

            