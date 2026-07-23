class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bkt = [[] for _ in range(len(nums)+1)] #list length
        for num, freq in count.items():
            bkt[freq].append(num)
        
        result=[]
        for r in range(len(bkt) -1,0,-1): #frequency high to low
            for num in bkt[r]:
                result.append(num)
                if len(result)==k:
                    return result
        return result


        