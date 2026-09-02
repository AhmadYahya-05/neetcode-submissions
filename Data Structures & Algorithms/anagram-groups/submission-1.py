from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_map = defaultdict(list)

        for word in strs:
        
            sorted_word = "".join(sorted(word)) 
            sorted_map[sorted_word].append(word)

        return list(sorted_map.values())

