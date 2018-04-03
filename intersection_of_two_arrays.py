class Solution(object):
    def intersect(self, nums1, nums2):
        num1_count = {}
        num2_count = {}
        #nums1= [1,1,1,1,2,2]
        #nums2 = [1,1,2]
        for num in nums1:
            if num in num1_count:
                num1_count[num]+=1
            else:
                num1_count[num]=1
        for num in nums2:
            if num in num2_count:
                num2_count[num]+=1
            else:
                num2_count[num]=1
        count_list = [num1_count.keys(), num2_count.keys()]
        iter_list = max(count_list, key = len)
        result = []
        #print iter_list
        for i in iter_list:
            occurences_nums1 = num1_count.get(i, 0) 
            occurences_nums2 = num2_count.get(i, 0)
            result.extend([i]*min(occurences_nums1,occurences_nums2))
        return result
            
            
                       
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        