class Solution(object):
    def plusOne(self, digits):
    	summand = 1
    	result = []
    	for ind, no in reversed(list(enumerate((digits)))):
    		s = no+summand
    		if s < 10:
    			result.append(s)
    			summand = 0
    			break
    		else:
    			result.append(0)
    		summand = 1 if s > 9 else 0
    	return [1]+digits[:ind]+list(reversed(result)) if summand == 1 else digits[:ind]+list(reversed(result))
    	
 






if __name__ == "__main__":
	a = [1,2,3]
	a = [9,9]
	#a = [1,2,3]
	print Solution().plusOne(a)

