
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {element : index}
        seen = {}
        for index, el in enumerate(nums):
            comp = target - el
            if comp in seen: 
                return  [seen[comp], index]
            seen[el] = index
        
        return []
        
            