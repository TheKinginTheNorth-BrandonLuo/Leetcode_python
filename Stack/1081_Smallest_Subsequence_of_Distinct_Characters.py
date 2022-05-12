'''
1081. Smallest Subsequence of Distinct Characters

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Input: s = "bcabc"
Output: "abc"
'''
class Solution:
    def smallestSubsequence(self, s):
        hash_table = {}
        for i in range(len(s)):
            hash_table[s[i]] = i
            
        stack = []
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
                
            while stack and stack[-1] > s[i] and hash_table[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
                
            stack.append(s[i])
            seen.add(s[i])
            
        return "".join(stack)