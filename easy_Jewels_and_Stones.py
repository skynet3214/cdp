from collections import Counter 
class Solution(object):
    def numJewelsInStones(self, J, S):
        stones_type_count = Counter(S)
        result = 0
        for char in J:
            result+=stones_type_count[char]
        return result

            
'''
Input: J = "aA", S = "aAAbbbb"
Output: 3



You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''