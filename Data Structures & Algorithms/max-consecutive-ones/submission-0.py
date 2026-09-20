class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lenT=0
        curr_len=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_len+=1
            else:
                curr_len=0
            if curr_len>lenT:
                lenT=curr_len
        return lenT