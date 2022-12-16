from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
   for i in range(len(nums)-1):
      if nums[i] + nums[i+1] == target:
         print([i, i+1]);

twoSum([2,7,10,11], 21);