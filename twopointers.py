#Valid Palindrome

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        return newStr == newStr[::-1]

#3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i, a in enumerate(nums): #this is helping us skip any dupicates that is above the index i
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1 #

            while l < r:
                answer = a + nums[l] + nums[r] # if previous count plus left nums plus nums right = ans
                if answer < 0:
                    l += 1
                elif answer > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])  
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:#checks through the continous loop to skip duplicate for the other []
                        l += 1
        return res 
        

#Contains With Most Water

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l <= r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
    
#Two Integer Sum

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            answers = numbers[i] + numbers[j]
            if answers > target:
                j -= 1
            elif answers < target:
                i += 1
            else:
                return [i + 1, j + 1] #append the plus 1 index based off one iondex count 