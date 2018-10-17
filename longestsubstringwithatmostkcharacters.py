class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
    	if not s or not k: 
            return 0
        head, tail = 0, 0
        longestsubstrlen, tmp_longestsubstrlen = 0, 0
        if len(set(s)) <=k:
            return len(s)
        #print head, tail
        while head < len(s):
            
            while tail <= len(s):
                #print "in tail"
                print "head:{}, in_Tail :: {}".format(head, tail)
                if longestsubstrlen > tail - head:
                    #tail+=1

                    break
                if len(set(s[head:tail])) <= k:
                    print "str:{}".format(s[head:tail])
                    print head, tail, tail-head
                    longestsubstrlen = tail-head if tail-head >= longestsubstrlen else longestsubstrlen 
                else:
                    tail+=1
                    break
                tail+=1
            head+=1
            #tail-=1
            #tail=head+longestsubstrlen
            print "end_Tail :: {}".format(tail)
        print "longestsubstrlen :: {}".format(longestsubstrlen)

        return longestsubstrlen
                
                

Solution().lengthOfLongestSubstringKDistinct("abaccc", 2)
print "rightfile"


#Input: s = "eceba", k = 2
#Output: 3
#Explanation: T is "ece" which its length is 3.