class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx=0
        while len(numbers)>0:
            num=numbers.pop()
            sum=num+numbers[idx]
            while sum<target:
                idx=idx+1
                sum=num+numbers[idx]
            if sum>target:
                continue
            elif sum==target:
                return [idx+1,len(numbers)+1]
        