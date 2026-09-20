class Solution:

    def encode(self, strs: List[str]) -> str:
        str_lens=[]
        
        for string in strs:
            str_lens.append(str(len(string))+',')
        encoded_str="?#?"
        encoded_str+=''.join(strs)
        encoded_str+="?#?"
        encoded_str+="".join(str_lens)
        print(encoded_str)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        encoded_list=s.split("?#?")
        #Element 1 is the raw string
        e0=encoded_list[1]
        print(e0)
        #Elements 2:k are the splits
        curr_index=0
        list_out=[]
        for e in encoded_list[2:]:
            print(e)
            next_set=e.split(',')
            print(next_set)
            for i in next_set:
                if i!='':
                    i_num=int(i)
                    list_out.append(e0[curr_index:curr_index+i_num])
                    curr_index+=i_num
        return list_out
