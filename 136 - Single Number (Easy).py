class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        
        for n, freq in hashMap.items():
            if freq == 1:
                return n