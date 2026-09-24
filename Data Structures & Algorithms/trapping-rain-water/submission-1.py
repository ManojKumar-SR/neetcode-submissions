class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0

        for i in range(len(height)):

            while stack and stack[-1][1] <= height[i]:
                ind, val = stack.pop()
                if not stack:
                    break

                total += (min(height[i],stack[-1][1]) - val) * (i - stack[-1][0] - 1)
            
            stack.append((i,height[i]))
        
        return total
            