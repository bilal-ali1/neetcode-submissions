class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN, closeN = 0, 0
        res = []
        sol = []

        def backtrack(openN, closeN):
            if openN == closeN and openN == n:
                res.append("".join(sol))
                return
            if openN < n:
                sol.append("(")
                backtrack(openN + 1, closeN)
                sol.pop()
            if closeN < openN:
                sol.append(")")
                backtrack(openN, closeN + 1)
                sol.pop()


        backtrack(0, 0)
        return res


            