class Solution:
    def minOperations(self, logs: List[str]) -> int:
        move = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                move -= 1 if move > 0 else 0
            elif logs[i] == "./":
                continue
            else:
                move += 1

        return move

        # other method by saving the path
        """
        class Solution:
    def minOperations(self, logs: List[str]) -> int:
        move = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                move -= 1 if move > 0 else 0
            elif logs[i] == "./":
                continue
            else:
                move += 1

        return move
        """
            

