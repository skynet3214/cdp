from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        
        def iterate_thro_all_window_sizes(start, s, t, char_count_t, char_count_s, max_window_size):

            min_window_size  = len(t)
            j = start
            print "start:{}".format(start)

            #for j in range(start, start+max_window_size, 1):
            while j < start+max_window_size:
                if j < len(s):
                    char_count_s[s[j]]+=1
                    missing, verify = compare_str(char_count_s, char_count_t)
                    if verify:
                        current_soln = s[start:j+1]
                        return missing, current_soln

                j+=1
                        
            return missing, ""
        
        def compare_str(char_count_s, char_count_t):
            missing = 0
            print "**"*20
            print char_count_s
            print "--"*10
            print char_count_t 
            
            for c in char_count_t.keys():
                if char_count_s.get(c,0) < char_count_t[c]:
                    missing += char_count_t[c] - char_count_s.get(c,0)
                    #print "returning none"
            print missing
            if missing == 0:
                return missing, True
            else:
                return missing, None

           
            #print "retruning true"
            
        char_count_t = {}
        char_count_s = {}
        for char in t:
            if char in char_count_t:
                char_count_t[char] += 1
            else:
                char_count_t[char] = 1
        #print "000"*20
        #print char_count_t
        
        max_window_size = len(s)
        char_count_s = defaultdict(int)

        #all_sols = []
        soln = ""
        start = 0 
        #for start in range(len(s)-len(t)+1):
        while start < len(s)-len(t)+1:
            missing,current_soln = iterate_thro_all_window_sizes(start, s, t, char_count_t, char_count_s, max_window_size)
            #print "missing:{}, current_soln:{}".format(missing, current_soln)
            if len(current_soln) == len(t):
                return current_soln
            if len(current_soln) > 0 and len(current_soln) <= max_window_size:
                soln = current_soln
                max_window_size = len(current_soln)
            char_count_s.clear()
            #start+=missing
            
            if missing>1:
                start+=missing
            else:
                start+=1
            
                
            print "start:{},missing:{}".format(start,missing)

                #all_sols.append(soln)
        #print "all solns::{}".format(all_sols)
        #print soln
        return soln


        


if __name__ == "__main__":
    #S = "aaaaaaaaaaaabbbbbcdd"
    #T = "abcdd"
    S = "aa"
    T = "a"
    #S = "ABC"
    #T = "AB"
    S = "ADOBECODEBANC"
    T = "ABC"
    print "String:{}, {}, substr:{},{}".format(S,len(S),T,len(T))
    print "This is the solution: {}".format(Solution().minWindow(S,T))

'''
corner cases/mistakes made:
string indices!!!!!! count count count just be careful! 
if any char in substr not at all present in the bigger string, key error while comparison. best way is to use default dict with default values or atleast use get
Test cases: 
S,T 
a,a
a,b
a,aa
both dictionaries need not be the same but 
'''
