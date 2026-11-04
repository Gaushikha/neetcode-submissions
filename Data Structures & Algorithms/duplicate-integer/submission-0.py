class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for value in nums:
            if value not in hash:
                hash[value]=1
            else:
                return True
        return False

        