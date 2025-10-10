class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = x < 0
        
        if x < 0: 
           x *= -1
        elif x == 0:
            return x
            
        while x % 10 == 0: 
            x = x// 10 
            

        # Reversing process  
        while x > 0: 
            reverse = (reverse * 10) + (x % 10) 
            x = x // 10 

        if reverse > (2 ** 31) -1: 
            return 0
        
        if negative: 
            reverse *= -1

        return reverse
        
