class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = []

        for i in range(len(heights)):
            area = 0
            ind_current = i
            while stack and stack[-1][1] > heights[i]:
                ind, val = stack.pop()
                area =  val * (i - ind)
                max_area = max(area,max_area)
                ind_current = ind

            stack.append((ind_current, heights[i]))
        
        for i, val in stack:
            max_area = max(max_area, val * (len(heights) - i))

        return max_area

