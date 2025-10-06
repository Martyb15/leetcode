class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # We need the second half of x and need to reverse it 
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10.  # Multiplying by 10 will move number(s) to the left one place 
            x = x // 10
       
            

        # When odd number of digits reverse will hold the middle digit
        # which is removed with "// 10"
        return x == reverse or x == reverse // 10


            
         #  -- Odd case --                -- Even case --      
            # x      rev                   x       rev
            # 12821   0                    9449    0
            # 1282    1                    944     9
            # 128     12                   94      94 (c not > rev)
            # 12      128 (x not > rev)     


        