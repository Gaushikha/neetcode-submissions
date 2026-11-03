class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for word in strs:
            sorted_char=sorted(word)
            j=" ".join(sorted_char)
            if j not in hash:
                hash[j]=[]
            hash[j].append(word)
        return list(hash.values())
        
