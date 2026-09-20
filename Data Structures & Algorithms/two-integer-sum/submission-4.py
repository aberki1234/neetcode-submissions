class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j,n in enumerate(nums):
            for i,m in enumerate(nums[j+1:], start=j+1):
                if n+m==target:
                    return [j, i]