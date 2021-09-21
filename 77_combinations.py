"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        self.backtrack([], 1, n, k, ans)
        
        return ans
        
    def backtrack(self, curr, start, n , k, ans):
        if len(curr) == k:
            ans.append(curr.copy())
            return
        
        for start in range(start, n+1):
            curr.append(start)
            self.backtrack(curr, start + 1, n, k, ans)
            curr.pop()
            
solution = Solution()

print(solution.combine(5, 3))
# [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]