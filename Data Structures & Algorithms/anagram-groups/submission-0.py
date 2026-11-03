class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            anagram_array= [0] * 26 
            for j in i:
                anagram_array[ord(j)-97]+=1
            if(tuple(anagram_array) in hashmap):
                hashmap[tuple(anagram_array)].append(i)
            else:
                hashmap[tuple(anagram_array)]=[]
                hashmap[tuple(anagram_array)].append(i)
        return(list(hashmap.values()))
        
