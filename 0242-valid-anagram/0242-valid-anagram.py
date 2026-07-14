class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #length different false
            return False
        counts = {}
        for char in s:
            #get all characters
            counts[char] = counts.get(char,0)+1;
        for ch in t:
            if ch not in counts:
                return False
            counts[ch] -=1
            if counts[ch] ==0:
                del counts[ch]
        return len(counts) == 0

