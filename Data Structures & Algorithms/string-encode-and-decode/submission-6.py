class Solution:

    def encode(self, strs: List[str]) -> str:
        returnstr = ""
        for string in strs:
            toAppend = str(len(string)) + '#' + string
            returnstr += toAppend
        return returnstr
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        returnList = []
        while i < len(s):
            while not s[j] == '#':
                j += 1
            strlen = int(s[i:j])
            string = s[j + 1 : j + 1 + strlen]
            returnList.append(string)
            i = j + 1 + strlen
            j = i
        
        return returnList
