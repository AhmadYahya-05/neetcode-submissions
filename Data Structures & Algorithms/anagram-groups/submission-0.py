#from collections import defaultdict
#from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap with sorted words as the key
        sorted_key_map = defaultdict(list)

        for word in strs:
            sorted_str = "".join(sorted(word))
            sorted_key_map[sorted_str].append(word)
    
        return list(sorted_key_map.values())

    

    