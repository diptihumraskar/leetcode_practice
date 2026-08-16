class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mag_count = Counter(magazine)
        ran_count = Counter(ransomNote)

        for char, count in ran_count.items():
            if mag_count[char] < count:
                return False
        return True

        