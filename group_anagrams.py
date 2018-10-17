
'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
    	ans = collections.defaultdict(list)
    	for s in strs:
    	    count = [0] * 26
    	    for c in s:
    	        count[ord(c) - ord('a')] += 1
    	    ans[tuple(count)].append(s)
    	return ans.values()
    	    
    	   


        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

if __name__ == "__main__":
	S = Solution()
	S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
