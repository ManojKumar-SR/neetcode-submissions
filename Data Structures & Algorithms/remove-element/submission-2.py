class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)
        if len(nums) == 0:
            return 0
        while i < j:
            if nums[i] == val:
                for k in range(i+1,j):
                    temp = nums[k-1]
                    nums[k-1] = nums[k]
                    nums[k] = temp
                j -= 1
            else:
                i += 1
        print(nums)
        return j 