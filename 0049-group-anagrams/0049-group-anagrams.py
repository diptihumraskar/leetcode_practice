class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         groups = defaultdict(list)

         for s in strs:
            key = ''.join(sorted(s))   # canonical form: sorted letters
            groups[key].append(s)

         return list(groups.values())
        