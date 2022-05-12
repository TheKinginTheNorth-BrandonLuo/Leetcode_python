'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    def minCut(self, s):
        dp = [(i - 1) for i in range(len(s) + 1)]
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                tmp = s[j : i]
                if tmp == tmp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]