class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for index,value in enumerate(nums):
            complement=target-value
            if complement in hash:
                return [hash[complement],index]
            else:
                hash[value]=index

        