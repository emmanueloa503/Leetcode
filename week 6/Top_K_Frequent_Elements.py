class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums) 
        freq = [[] for _ in range(len(nums) + 1)] 
        
        for num, cnt in count.items():
            freq[cnt].append(num)  
        
        res = []
        for i in range(len(freq) - 1, 0, -1):  
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res        