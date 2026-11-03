class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
       let hash={};
        let j;
        for (const i of strs){
            j=i.split('').sort().join();
            if(j in hash)
            hash[j].push(i);
            else
            hash[j]=[i];
        }
        return Object.values(hash)
    }
}
