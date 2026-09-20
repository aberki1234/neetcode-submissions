class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        idx=0
        return_list=[]
        numbers = list(numbers)
        while len(numbers)>0 and idx<len(numbers)-1:
            num=numbers.pop()
            sum=num+numbers[idx]
            while sum<target and idx<len(numbers)-1:
                idx=idx+1
                sum=num+numbers[idx]
            if sum>target:
                continue
            elif sum==target:
                return_list.append(sorted([-target,num,numbers[idx]]))
        return return_list
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        triplets=[]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            init_num=nums[i]
            triplets.extend(self.twoSum(nums[i+1:],-init_num))
        #Deduplicate triplets
        triplets = [list(t) for t in {tuple(lst) for lst in triplets}]
        return triplets