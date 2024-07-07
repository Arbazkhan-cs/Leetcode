class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        remainingBottles = numBottles

        while remainingBottles >= numExchange:
            newBottles = remainingBottles // numExchange
            totalBottles += newBottles
            remainingBottles = newBottles + (remainingBottles % numExchange)
        
        return totalBottles
        