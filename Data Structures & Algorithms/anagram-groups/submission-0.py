class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        return_list = []
        for i in range(len(strs)):
            anagram = ''.join(sorted(list(strs[i])))
            if anagram not in ana_dict:
                ana_dict[anagram] = [strs[i]]
                return_list.append([strs[i]])
            else:
                ana_dict[anagram].append(strs[i])

        return ana_dict.values()
