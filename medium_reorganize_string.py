'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
Input: S = "aaab"
Output: "

Input: S = "aab"
Output: "aba"
'''
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
    	char_count_d = Counter(S)
    	ord_coll = [pair[0] for pair in char_count_d.most_common(len(S))]
    	if len(S)%2:
    		max_occurences = (len(S)/2)+1
    	else:
    		max_occurences = (len(S)/2)

    	result = ['-']*len(S)

    	if max(char_count_d.values()) > max_occurences:
    		print "returning empty string"
    		return ''
    	else:
    		start = 0
    		for char in ord_coll:
    			i = start
    			while char_count_d[char] > 0:
    				if i < len(S):
    					result[i] = char
    				char_count_d[char]-=1
    				i+=2
    			#print result
    			if '-' in result:
    				start = result.index('-') 


    	return ''.join(result)

        """
        :type S: str
        :rtype: str
        """

if __name__ == "__main__":
	Inst = Solution()
	S = 'vvvlo'
	S = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
	result = Inst.reorganizeString(S)
	print "aCtual count::"
	print Counter(S)
	print result
	print Counter(result)