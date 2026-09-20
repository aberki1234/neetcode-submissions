class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod=1
        zero_indices=[]
        HAS_ZERO=False
        for i,num in enumerate(nums):
            if num!=0:
                total_prod*=num
            else:
                zero_indices.append(i)
        print(total_prod)
        output_list=[]
        for i,num in enumerate(nums):
            if num!=0 and len(set(zero_indices)-set([i]))==0:
                output_list.append(int(total_prod/num))
            elif num!=0 and len(set(zero_indices)-set([i]))>=0:
                output_list.append(0)
            elif num==0 and len(set(zero_indices)-set([i]))==0:
                output_list.append(int(total_prod))
            else:
                output_list.append(0)
        return output_list