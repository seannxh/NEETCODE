# Contains Duplicate 
from collections import defaultdict
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []

        for num in nums:
            if num in res:
                return True
            res.append(num)
        return False

#Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26 

        for idx, char in enumerate(s):
            countS[ord(char) - ord("a")] += 1
            countS[ord(t[idx]) - ord("a")] -= 1

        return sum(countS) == 0
    
#Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in res:
                return [res[answer], i]
            res[nums[i]] = i       

#Group Anagram
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(word)
        return res.values()
#Top K Freq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq =  [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
#Encode & Decode 
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res
            
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
#Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        answer = [1] * len(nums)

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range((n) -2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer
# Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if  (board[r][c] in row[r]
                    or board[r][c] in columns[c]
                    or board[r][c] in square[(r // 3, c //3)]):
                    return False

                columns[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
                
        return True    
#Largest Consecutive 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)

        longest = 0

        for n in nums:
            if (n - 1) not in setNum:
                length = 0 
                while (n + length) in setNum:
                    length += 1
                longest = max(length, longest)
        return longest
n = 10
step = 2 if n % 2 == 0 else 1
res = [i for i in range(1, n + 2, step)]


print(res)