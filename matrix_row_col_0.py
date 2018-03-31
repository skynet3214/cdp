class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        if matrix:
            n = len(matrix[0])
        col_nos = set()
        row_nos = set()
        for row_no, row in enumerate(matrix):
            if 0 in row:
                row_nos.add(row_no) 
                for col in range(n):
                    if matrix[row_no][col] == 0:
                        col_nos.add(col)
                #set all elements in the row to 0  
                     
                matrix[row_no] = [0]*n
        #set all columns in matrix to 0
        
        for i in range(m):
            if i not in row_nos:
                for j in col_nos:
                    matrix[i][j] = 0
            

        print matrix 

if __name__ == "__main__":
    matrix = [[1,2,3],[0,1,1]]
    Solution().setZeroes(matrix)


            



                
                
        
                
                
