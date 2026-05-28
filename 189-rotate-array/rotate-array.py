class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums) 
        #taking because we need k < len(nums) but if k>=len(nums) so k becomes 0 and arrya is reversed from 0th pos which means it is fully rotated

        ranges = [
        (0, len(nums)-1),         #to nums.reverse()
        (0, k-1),                 #to nums[:k] = reversed(nums[:k])
        (k, len(nums)-1)          #tonums[k:] = reversed(nums[k:]) 
        ]

        for l,r in ranges:
            while l<r:
                nums[l], nums[r]=nums[r], nums[l] #python stores RHS into a temp tuple to assign to LHS
                l, r = l+1, r-1

