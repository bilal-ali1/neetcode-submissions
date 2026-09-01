class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ret = []
        while i < len(word1) and j < len(word2):
            ret.append(word1[i])
            ret.append(word2[j])
            i += 1
            j += 1
        if i < len(word1):
            ret.append(word1[i:])
        if j < len(word2):
            ret.append(word2[j:])
        return "".join(ret)