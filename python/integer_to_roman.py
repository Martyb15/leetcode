class Solution:
    def intToRoman(self, num: int) -> str:
        r_string = ''
        while num > 0:
            if num >= 1000: 
                r_string += 'M'
                num -= 1000
            elif num >= 900:
                r_string += 'CM'
                num -= 900
            elif num >= 500:
                r_string += 'D'
                num -= 500
            elif num >= 400:
                r_string += 'CD'
                num -= 400
            elif num >= 100: 
                r_string += 'C'
                num -= 100
            elif num >= 90:
                r_string += 'XC'
                num -= 90
            elif num >= 50:
                r_string += 'L'
                num -= 50
            elif num >= 40:
                r_string += 'XL'
                num -= 40
            elif num >= 10:
                r_string += 'X'
                num -= 10 
            elif num == 9: 
                r_string += 'IX'
                num -= 9
            elif num >= 5:
                r_string += 'V'
                num -= 5
            elif num == 4:
                r_string += 'IV'
                num -= 4
            elif num  >= 1:
                r_string += "I"
                num -= 1
        return r_string
        
# Could use list instead of string (keeping mutability in mind)
# list would require use of .join() method.
                
        