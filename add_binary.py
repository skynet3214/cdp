class Solution(object):
    def addBinary(self, a, b):
        a = '11'
        b = '1'
        def binary_logic(a1, b1, c ):
            a1 = str(a1)
            b1 = str(b1)
            c = str(c)
            if a1=='1' and b1 =='1' and c =='0':
                print 'I am here in 110'
                s, carry = 0,1
            elif a1 == '1' and b1 == '1' and c == '1':
                print 'I am here in 111'
                s, carry = 1,1
            elif a1 == '0' and b1 == '0' and c == '0':
                print 'I am here in 000'
                s, carry = 0, 0
            elif a1 == '0' and b1 == '0' and c == '1':
                print 'I am here in 001'
                s, carry = 1, 0
            elif a1 == '1' and b1 == '0' and c == '0':
                print 'I am here in 100'
                s, carry = 1, 0
            elif a1 == '1' and b1 == '0' and c == '1':
                print 'I am here in 101'
                s, carry = 0, 1
            elif a1 == '0' and b1 == '1' and c == '0':
                print 'I am here in 010'
                s, carry = 1, 0
            elif a1 == '0' and b1 == '1' and c == '1':
                print 'I am here in 011'
                s, carry = 0, 1
            else:
                s, carry = 0, 0
                
            return str(s), str(carry)
        
        carry = 0 
        
        longer = max(a,b)
        smaller = min(a,b)
        padding = '0'*(len(longer)-len(smaller))
        new_smaller = padding+smaller
        i_c = 0 
        s=0
        result = []
        print longer, new_smaller
        for i in range(len(longer)-1,-1, -1):
            
            
            s, i_c = binary_logic(longer[i],new_smaller[i], i_c)
            
            result.append(s)
        result.append(i_c)
        result_str = ''.join(reversed(result))
        
        return result_str
            
            
        
        
        