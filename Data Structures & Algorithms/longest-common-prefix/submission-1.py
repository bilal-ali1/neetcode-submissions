class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommon = strs[0]
        for str in strs[1:]:
            pref = ""
            for i in range(min(len(longestCommon), len(str))):
                if str[i] == longestCommon[i]:
                    pref = pref + str[i]
                else:
                    break
            longestCommon = pref
        return longestCommon