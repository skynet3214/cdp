class Solution(object):
    def removeDuplicates(self, nums):
        if nums:
            if len(nums) > 1:
                current_element, i = nums[0],1 
            else:
                current_element = nums[0]
                return 1
        else:
            return 0
        while i < len(nums):
            if current_element == nums[i]:
                del nums[i]
            else:
                current_element = nums[i]
                i+=1
        return len(nums)
            
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
        