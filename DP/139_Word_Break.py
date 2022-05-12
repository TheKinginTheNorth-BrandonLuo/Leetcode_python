'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    def wordBreak(self, s, wordDict):
        d = set(wordDict)
        n = len(s)

        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for start in range(n):
            if dp[start] != True:
                continue
            for end in range(start + 1, n + 1):
                if s[start: end] in d:
                    dp[end] = True
                    
        return dp[-1]