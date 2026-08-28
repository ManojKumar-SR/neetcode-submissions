class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        for i in tokens:
            if i == "*":
                st.append(st.pop()*st.pop())
            elif i=="/":
                v = st.pop()
                st.append(int(st.pop()/v))
            elif i=="+":
                st.append(st.pop()+st.pop())
            elif i=="-":
                v = st.pop()
                st.append(st.pop()-v)
            else:
                st.append(int(i))
        
        return st[-1]