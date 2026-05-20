class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            ret += str(len(string)) + "#" + string
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        j = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strlen = int(s[i:j])
            ret.append(s[j + 1: j + 1 + strlen])
            i = j + 1 + strlen
        return ret