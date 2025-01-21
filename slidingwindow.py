
from typing import List

#Best Time to Buy & Sell Stocks
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float('inf')
        
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)

            profit = prices[i] - minPrice

            res = max(res, profit)
        return res
    
#Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - ord("A")] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1

            longest = max(longest, (r - l + 1)) 
        return longest
