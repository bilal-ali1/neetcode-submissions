class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        # go through words pair by pair
        for i in range(len(words) - 1):
            wrd1 = words[i]
            wrd2 = words[i + 1]
            minLen = min(len(wrd1), len(wrd2))
            if (len(wrd1) > len(wrd2)) and wrd1[:minLen] == wrd2[:minLen]:
                return ""
            
            for j in range(minLen):
                if wrd1[j] != wrd2[j]:
                    adj[wrd1[j]].add(wrd2[j])
                    break
            
        visit = {} # [char : bool], true if in current path, false if not
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
            
