class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lp = 0
        result = 0
        char_set = set()

        for rp in range(len(s)):
            while s[rp] in char_set:
                char_set.remove(s[lp])
                lp += 1

            char_set.add(s[rp])
            result = max(result, rp - lp + 1)

        return result

