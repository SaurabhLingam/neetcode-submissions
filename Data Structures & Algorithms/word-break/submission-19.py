class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(len(s)+1):
            for word in wordDict:
                l = len(word)
                if i - l >= 0 and dp[i-l] == 1:
                    if s[i-l:i] in wordDict:
                        dp[i] = 1

        return True if dp[len(s)] == 1 else False