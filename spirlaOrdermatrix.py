class Solution(object):
    def spiralOrder(self, matrix):
    	if len(matrix) and len(matrix[0]):
    		no_of_rows, no_of_cols = len(matrix), len(matrix[0])
    	else:
    		no_of_cols, no_of_rows = 0, 0
    	for row in matrix:
    		if len(row) != no_of_cols:
    			print "not a valid matrix"
    			return None

    	left = 0
    	right = no_of_cols-1
    	top = 0
    	bottom = no_of_rows-1
    	elements = 0
    	results = []

    	print "no of elements:{}".format(no_of_rows*no_of_cols)
    	
    	while elements < no_of_rows*no_of_cols:

    		if top == bottom:
    			for i in range(left, right+1):
    				results.append(matrix[top][i])
    				elements+=1
    			print len(results),results
    			return results
    		
    		if left == right:
    			for i in range(top, bottom+1):
    				results.append(matrix[i][left])
    				elements+=1
    			print len(results),results
    			return results

    		for j in range(left, right):
    			print "(top,j):({},{})".format(top,j)
    			results.append(matrix[top][j])
    			elements+=1


    		for l in range(top, bottom):
    			print "(l,right):({},{})".format(l,right)
    			results.append(matrix[l][right])
    			elements+=1


    		for k in range(right, left, -1):
    			print "(bottom,k):({},{})".format(bottom,k)
    			results.append(matrix[bottom][k])
    			elements+=1
    		
    		for m in range(bottom, top, -1):
    			print "(m,left):({},{})".format(m,left)
    			results.append(matrix[m][left])
    			elements+=1

    		right -=1
    		left+=1
    		top+=1
    		bottom-=1
    		print "elements:{}".format(elements)
    		print "right:{}".format(right)
    		print "left:{}".format(left)
    		print "top:{}".format(top)
    		print "bottom:{}".format(bottom)
    	print len(results), results


        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
'''
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16 

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''
#matrix = [[7],[9],[6]]
#matrix = [[7,6,8]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix = [[1,2,3,4,20],[5,6,7,8,21],[9,10,11,12,22]]
#matrix = [[1,2,3],[4,5,6]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[1,1],[2,3,4]]
Solution().spiralOrder(matrix)