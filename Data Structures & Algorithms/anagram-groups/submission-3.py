class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {} # {} -> List[str]
        toReturn = []
        for str in strs:
            if "".join(sorted(str)) in anaDict:
                anaDict["".join(sorted(str))].append(str)
            else:
                anaDict["".join(sorted(str))] = [str]
        for lst in anaDict.values():
            toReturn.append(lst)
        return toReturn
