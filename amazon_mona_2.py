class Solution(object):
    def efficient_processor_usage(self, capacity, fg_apps, bg_apps):
    	max_usage, current_usage = 0, 0
    	app_results = []
    	for fg_app in fg_apps:
    		for bg_app in bg_apps:
    			
    			current_usage = fg_app[1] + bg_app[1]
    			if  current_usage <= capacity and current_usage >= max_usage:
    				if current_usage > max_usage:
    					app_results[:] = []
    				max_usage = current_usage
    				app_results.append([fg_app[0], bg_app[0]])
    	return app_results
    					
    					#print "In  > max_usage cap:{}, fg_id:{}, bg_id:{}, app_results:{}".format(capacity, fg_app[0], bg_app[0], app_results)
    					#print "In  > max_usage cap:{}, fg_id:{}, bg_id:{}, app_results:{}".format(capacity, fg_app[0], bg_app[0], app_results)
    	
    

if __name__ == "__main__":
	capacity = 10
	fg_apps = [[1,3], [2,5], [3,7], [4,8]]
	bg_apps = [[1,2], [2,3], [3,4], [4,5]]
	
	print Solution().efficient_processor_usage(capacity, fg_apps, bg_apps)
