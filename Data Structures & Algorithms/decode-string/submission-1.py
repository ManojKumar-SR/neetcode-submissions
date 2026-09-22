class Solution:
    def decodeString(self, s: str) -> str:
        st = []


        for i in s:
            if i == "]":
                text = ""
                
                while st[-1] != "[":
                    text = st.pop() + text
                
                st.pop()

                num = ""
                while st and st[-1].isdigit():
                    num = st.pop() + num
                
                if num :
                    text *= int(num)
                st.append(text)
            else:
                st.append(i) 
        
            #print(st)

        return "".join(st)
       