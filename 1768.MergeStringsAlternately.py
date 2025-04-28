'''
1768. Merge Strings Alternately (Easy)

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

'''

# Simply iterate over each characters from both strings and appending in result and converting result to string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Time complexity O(m + n), processing will be done in O(1), but we are adding strings so..
        # Space complexity O(m + n), as we are using res as an extra memory factor

        res = []

        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1


        # append any leftover words
        res.append(word1[i:])
        res.append(word2[j:])
        
        # res was initialized as an array in starting so all characters were stored in it, so converted res to string. 
        return ''.join(res)