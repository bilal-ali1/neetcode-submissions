class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = ""
        for s in strs:
            return_str += str(len(s)) + '#' + s
        print(return_str)
        return return_str

        
    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0
        j = 0
        while (i < len(s)):
            while not (s[j] == "#"):
                j += 1
            length = int(s[i:j])
            print(length)
            return_list.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            j = j + 1 + length
        return return_list

        

