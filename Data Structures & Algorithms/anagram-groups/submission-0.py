class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        equal_strs=strs.copy()
        for i,string in enumerate(strs):
            equal_strs[i]=sorted(string)
        #Separate out anagrams using hashmap
        hash_out={}
        for i,string in enumerate(equal_strs):
            if ''.join(string) not in hash_out.keys():
                hash_out[''.join(string)]=[strs[i]]
            else:
                hash_out[''.join(string)].append(strs[i])
        return list(hash_out.values())
