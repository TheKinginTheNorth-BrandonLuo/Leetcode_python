'''
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''
'''
initial dp matrix:
   0  r  o  s
0  0  1  2  3
h  1
o  2
r  3
s  4
e  5
'''
class Solution:
    def minDistance(self, word1, word2):
        len1, len2 = len(word1) + 1, len(word2) + 1
        
        dp = [[0 for i in range(len2)] for j in range(len1)]
        
        for i in range(len2):
            dp[0][i] = i
        for i in range(len1):
            dp[i][0] = i
        for i in range(1, len1):
            for j in range(1, len2):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
                
        return dp[-1][-1]