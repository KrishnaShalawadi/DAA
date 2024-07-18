class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for val in nums:
            count[val] = 1 + count.get(val, 0)
        arr = [[] for i in range(len(nums) + 1)]  
        for n, c in count.items():
            arr[c].append(n)
        res = []
        for i in range(len(arr) - 1, 0, -1): 
            for j in arr[i]:  
                res.append(j)
                if len(res) == k: 
                    return res
