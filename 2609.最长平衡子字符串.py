#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if s == '':
            return 0
        elif "0" not in s:
            return 0
        elif "1" not in s:
            return 0
        #正常可遍历情况
        #找到中心点0|1
        midl=s.find("01",0)
        max=0
        while midl!=-1:
            
            start=0
            countDiffusion=self.countDiffusion(s,midl)
            start=countDiffusion+midl
            midl=s.find("01",start)
            if countDiffusion>max:
                max=countDiffusion
        return max
    def countDiffusion(self,s,start):
        l=start
        r=start+1
        sum=2
        while l-1>=0 and r+1<len(s) :
            if s[l-1]=="0" and s[r+1]=="1":
                sum+=2
                l-=1
                r+=1
            else:
                break
        return sum

        #向两边扩散
        #记录最长长度
        #遍历完成
# @lc code=end

