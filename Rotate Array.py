class Solution(object):
    def rotate(self, nums, k):
    	if not nums: 
    		return 0 
    	k = k if k < len(nums) else k%n
    	buff = nums[-k-1:-1]
    	for i in range(k, len(nums), k):
    		

    	



if __name__ == "__main__":
	nums, rotate = [1,2,3,4,5,6,7], 3
	print Solution().rotate(nums, rotate)
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    '''
        456
        645
        564

        4567
        7456
        6745
        5674
        '''