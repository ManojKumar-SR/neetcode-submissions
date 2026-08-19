class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = defaultdict(int)

        for i in nums:
            h[i] += 1
            print(h[i])
            if h[i] >= (len(nums)//2 + 1):
                return i
        