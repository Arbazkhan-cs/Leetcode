class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        res = [[1]]
        for i in range(0, numRows-1):
            prev_row = [0] + res[i] + [0]
            temp = []
            for j in range(1, len(prev_row)):
                sum = prev_row[j] + prev_row[j-1]
                temp.append(sum)
            
            res.append(temp)

        return res




