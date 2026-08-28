class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []

        for i in asteroids:
            add = True
            while st and (st[-1]>=0 and i < 0):
                if (abs(st[-1]) < abs(i)):
                    st.pop()

                elif abs(st[-1]) == abs(i):
                    st.pop()
                    add = False
                    break
                else:
                    add = False
                    break
                
            if add:
                st.append(i)
                        
        return st
