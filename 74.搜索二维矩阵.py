# @before-stub-for-debug-begin
from python3problem74 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
import bisect
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        col0=[row[0] for row in matrix]
        target_row=bisect.bisect_right(col0,target)-1
        if target_row<0:
            return False
        target_col=bisect.bisect_left(matrix[target_row],target)
        if target_col>=n:
            return False
        if matrix[target_row][target_col]==target:
            return True
        return False
        

# @lc code=end
#region 二分查找
#first version:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
    #     for v in matrix:
    #         if v[0]<=target and v[-1]>=target:
    #             return self.binarySearch(v,target)
    #     return False
    # def binarySearch(self,nums,target):
    #     l=0
    #     r=len(nums)-1
    #     while l<=r:
    #         mid=(l+r)//2
    #         if nums[mid]==target:
    #             return True
    #         elif nums[mid]>target:
    #             r=mid-1
    #         else:
    #             l=mid+1
    #     return False
#endregion

#region second version:
        # m,n=len(matrix),len(matrix[0])
        # l,r=0,m*n-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if matrix[mid//n][mid%n]==target:
        #         return True
        #     elif matrix[mid//n][mid%n]>target:
        #         r=mid-1
        #     else:
        #         l=mid+1
        # return False     
#endregion

