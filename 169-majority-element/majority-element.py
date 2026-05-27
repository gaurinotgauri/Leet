from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        maxkey=max(count, key=count.get)
        return maxkey