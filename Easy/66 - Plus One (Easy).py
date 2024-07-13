class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in digits:
            num = (num*10) + n
        
        num += 1
        res = []
        for n in str(num):
            res.append(int(n))
        return res
