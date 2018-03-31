from collections import defaultdict
from pprint import pprint
final_results = []
def combinationSum(candidates, target, results, level):
	dp_dict = {}
	for num in range(1, target+1, 1):
		dp_dict[num] = []
	#print dp_dict
	
	for candidate in candidates:
		if  candidate < target:
			dp_dict[candidate].append([candidate])
	#print dp_dict
	
	
	for num in range(1,target+1,1):
		for sub_p in range(1,num):
			#print sub_p
			
			for soln in dp_dict[sub_p]:
				#print "soln:{}".format(soln)
				for candidate in candidates:
					#print "candidate:{}, sum(soln):{}".format(candidate, sum(soln))
					if candidate!= num and  sum(soln)+candidate == num:
						dp_dict[num].append(soln + [candidate])
			
			

	#pprint(dp_dict)
	pprint(dp_dict[target])



			

if __name__ == "__main__":
	candidates = [3,2,4]
	target = 50
	results = []
	i = 0
	combinationSum(candidates, target, results, i)
	
	