class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set=list(set(nums))
        nums_count={}
        for i in nums_set:
            nums_count[i]=0
        for n in nums:
            nums_count[n]+=1
        #Returns k best vals- now need k best keys
        return [
            num
            for num, frequency in sorted(
                nums_count.items(),
                key=lambda pair: pair[1],
                reverse=True
            )[:k]
        ]