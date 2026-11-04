class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s=sorted(s)
        sorted_t=sorted(t)
        str1=" ".join(sorted_s)
        str2=" ".join(sorted_t)
        if str1==str2:
            return True
        return False
        