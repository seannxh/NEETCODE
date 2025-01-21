

#Binary search only works on sorted arrays 
# We would get for example if array is 1 - 50 we guess 25 because it know if the number is > or < than 25
# We usually retun the index

import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r ) // 2
            if nums[m] < target:
                l = l + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
            


binary = [1, 3, 3, 4, 5, 6, 7, 8]
target = 5
# we want the boundaries


def binarySearch(binary, target):

    i, j = 0, len(binary) - 1
    while i <= j:
        m = (i + j) // 2

        if target > binary[m]:
            i = m + 1
        elif target < binary[m]:
            j = m - 1
        else:
            return m
    return -1

print(binarySearch(binary, target))

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 13

def searchMatrix(matrix, target):
        #Dobule bianry search

    rows, cols = (len(matrix)),   len(matrix[0])
    print(len(matrix[0]))
    top, bot = 0, rows - 1

    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            print(matrix[row][-1])
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, cols - 1
    print(cols - 1)
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False
    
print(searchMatrix(matrix, target))



matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 30

rows, cols = len(matrix), len(matrix[0])  # rows = 3, cols = 4

top, bot = 0, rows - 1  # Correctly set bot to rows -1

while top <= bot:
    row = (top + bot) // 2  # Correct calculation of the middle row
    print(f"Checking row {row}: {matrix[row]}")
    
    if target > matrix[row][-1]:
        print(f"Target {target} is greater than the last element of row {row}: {matrix[row][-1]}")
        top = row + 1
    elif target < matrix[row][0]:
        print(f"Target {target} is less than the first element of row {row}: {matrix[row][0]}")
        bot = row - 1
    else:
        print(f"Target {target} is within row {row}: {matrix[row]}")
        # Perform binary search within the row
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            print(f"  Checking element at column {m}: {matrix[row][m]}")
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                print(f"Target {target} found at row {row}, column {m}.")
                break
        else:
            print(f"Target {target} not found in row {row}.")
        break
else:
    print(f"Target {target} not found in the matrix.")


count = 5
k = 3
p = 5
count += math.ceil(float(p) / k)
print(count)

print(math.ceil(5))

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Determines the minimum eating speed (k) such that Koko can eat all the bananas within h hours.

        Args:
        - piles (List[int]): A list where each element represents the number of bananas in a pile.
        - h (int): The total number of hours Koko has to eat all the bananas.

        Returns:
        - int: The minimum integer k representing the bananas-per-hour eating rate.
        """
        # Initialize the lower and upper bounds for binary search
        left, right = 1, max(piles)
        result = right  # Start with the maximum possible eating speed

        # Perform binary search to find the minimal k
        while left <= right:
            k = (left + right) // 2  # Current eating speed to test
            hours_needed = 0  # Total hours needed with current eating speed

            # Calculate the total hours needed to eat all piles at speed k
            for p in piles:
                hours_needed += math.ceil(p / k)

            # Debugging Statements (Optional)
            # Uncomment the lines below to see the internal state during execution
            # print(f"Testing k = {k}: Total hours needed = {hours_needed}")

            if hours_needed <= h:
                # If Koko can eat all bananas within h hours with speed k,
                # try to find a smaller k for optimality
                result = k
                right = k - 1
            else:
                # If Koko cannot eat all bananas within h hours with speed k,
                # increase k to reduce the number of hours needed
                left = k + 1

        return result

# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    piles1 = [3, 6, 7, 11]
    h1 = 8
    print(f"Minimum eating speed for Test Case 1: {solution.minEatingSpeed(piles1, h1)}")
    # Expected Output: 4

    # Test Case 2
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    print(f"Minimum eating speed for Test Case 2: {solution.minEatingSpeed(piles2, h2)}")
    # Expected Output: 30

    # Test Case 3
    piles3 = [1, 2, 4, 8]
    h3 = 4
    print(f"Minimum eating speed for Test Case 3: {solution.minEatingSpeed(piles3, h3)}")
    # Expected Output: 8

#Search in Rotated Sorted Array 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # this checks if number is sorted
                if target > nums[m] or target < nums[l]: #checks if target is in the leftside of m if not 
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]: #checks if target is in the rightside of m if not 
                    r = m - 1
                else:
                    l = m + 1 # loops until it finds the minimum number of a sorted rotated array
        return -1
# Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l += 1
            else:
                r -= 1
        return res
    
# Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Dobule bianry search

        rows, cols = (len(matrix)), len(matrix[0]) #There are 3 rows and cols is starting at the first list  of the nested list
        top, bot = 0, rows - 1

        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, cols - 1
        rows = (top + bot) // 2
        while l <= r:
            m = (l + r) // 2
            if target > matrix[rows][m]:
                l = m + 1
            elif target < matrix[rows][m]:
                r = m - 1
            else:
                return True
        return False
        