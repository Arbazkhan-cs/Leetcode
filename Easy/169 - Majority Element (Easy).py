class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0)+1
        
        n = len(nums)//2
        for num, freq in hashMap.items():
            if freq > n:
                return num
        