from collections import defaultdict
final_results = []
dp_dict = defaultdict(list)
def combinationSum(candidates, target,index, results, level):
	level+=1
	#print candidates, target,index, results, level
	#print id(target),level
	if target == 0:
		#print "print id(results):{},result list:{}, level:{}".format(id(results),results,level)
		print "results:{}".format(results)
		final_results.append(results)
		#del results[:]
		return
	elif target < 0:
		#del results[:]
		return
	else:
		for i in range(index, len(candidates)):
			combinationSum(candidates, target-candidates[i],i, results+[candidates[i]],level)
		#for num in candidates:   
		#	combinationSum(candidates, target-num, results+[num],level)


if __name__ == "__main__":
	candidates = [3,2,4]
	target = 50
	results = []
	i = 0
	#candidates.sort()
	print candidates
	combinationSum(candidates, target,0, results, i)
	print "The results are:{}".format(final_results)
	

'''
read python global variables and pass by reference/whateevr it is.
passing results list and checking id, it shows the same id across recursive calls. so it is like pass by reference by default ?
appending a list to a list of lists and clearing the previous list, also clears the appended values. 
for ex: a = [], b = [1,2] a.append(b)=>a = [[1,2]], del b[:], now a = [[]]
'''

'''

3 - [1,2] 

1. for num in [1,2]:
	combinationSum([1,2], 3-1, [1])
	combinationSum([1,2]), 3-2, [2])

2. for num in [1,2]:
	combinationSum([1,2], 2-1, [1,1])
	combinationSum([1,2], 2-2, [1,2])

3. for num in [1,2]:
	combinationSum([1,2], 1-1, [1,1,1])
	combinationSum([1,2], 1-2, [1,1,2])
	level is complete 
1.2 for num in [1,2]: -- combinationSum([1,2], 1, [2])
combinationSum([1,2], 1-1, [2,1])
combinationSum([1,2], 1-2, [2,2])



--->combinationSum([1,2], 0, [1,1,1])
print results - return to 3 to process 2nd element of list

--->combinationSum([1,2], -1, [1,1,2])
target < 0 return

2.2 --->combinationSum([1,2], 2-2, [1,2])
print results return 
'''