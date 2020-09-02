from typing import List

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        i=0
        res =''
        while True:
            char=''
            for ind,item in enumerate(strs):
                if i>len(item)-1:
                    return res
                if ind==0:
                    char=item[i]
                elif char!=item[i]:
                    return res
            res+=char
            i+=1
        return res

if __name__=="__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    li=["flower","flow","flight"]
    for item in zip(*li):
        print(item)
    print(zip(*li))