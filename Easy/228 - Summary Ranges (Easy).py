class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        res = []
        for right in range(1, len(nums) + 1):
            prevVal = nums[right-1]
            if right == len(nums) or nums[right] != prevVal+1:
                if left == right - 1:
                    res.append(str(nums[left]))
                else:
                    res.append(f"{nums[left]}->{prevVal}")
                left = right
        
        return res

        
            
            
            
