class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        res=[]
        for i in nums2:
            while stack and i>stack[-1]:
                smaller=stack.pop()
                next_greater[smaller]=i
            stack.append(i)
        for num in nums1:
            res.append(next_greater.get(num,-1))
        return res
                
        