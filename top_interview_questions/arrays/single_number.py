"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List

class Solution:

    def singleNumberInitial(self, nums: List[int]) -> int:
        """
        My initial solution, using storage.
        """
        visited = {}
        for n in nums:
            if n not in visited.keys():
                visited[n] = 1
            else:
                visited[n] += 1
             
        for key in visited.keys():
            if visited[key] == 1:
                return key
    

    def singleNumber(self, nums: List[int]) -> int:
        """
        Final solution.
        This solution uses the communicative property of the XOR operation:
            A XOR A  == 0
            A XOR A XOR B == B
            A XOR B XOR A == B
            A ^ B ^ A ^ C ^ B  = (A ^ A) ^ (B ^ B) ^ C == C
        """
        result = 0
        for num in nums:
            result ^= num
        return result

    def testSolution(self):

        assert self.singleNumber([2, 2, 1]) == 1
        assert self.singleNumber([4, 1, 2, 1, 2]) == 4

if __name__ == '__main__':

    soln = Solution()
    soln.testSolution()