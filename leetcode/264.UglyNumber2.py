class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]

        idx2 = 0
        idx3 = 0
        idx5 = 0

        while len(ans) < n:
            num = min(ans[idx2]*2, ans[idx3]*3, ans[idx5]*5)
            ans.append(num)
            if num == ans[idx2]*2: idx2 += 1
            if num == ans[idx3]*3: idx3 += 1
            if num == ans[idx5]*5: idx5 += 1

        return ans[n-1]