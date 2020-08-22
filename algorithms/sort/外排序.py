"""
知乎解析
https://zhuanlan.zhihu.com/p/36618960

"""

import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        return dummy.next

    def adjust(self, s, listsLen, lists, loserTree):
        # 构成完全二叉树，按完全二叉树索引
        t = (s + listsLen) // 2
        # 比较当前节点和父节点的大小，若大于，则更新，并将胜者保存在索引0位置
        while t > 0:
            if lists[s].val > lists[loserTree[t]].val:
                s, loserTree[t] = loserTree[t], s
            t = t // 2
        loserTree[0] = s

    def merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 去掉list中的None
        while None in lists:
            lists.remove(None)
        # 若当前序列小于等于1，则返回结果
        listsLen = len(lists)
        if listsLen < 1:
            return None
        if listsLen == 1:
            return lists[0]
        # 使用内排序算法，归并路数不超过16，然后使用外排序进一步归并
        while len(lists) > 16:
            i, j = 0, len(lists) - 1
            while i < j:
                lists[i] = self.merge_two_lists(lists[i], lists[j])
                lists.pop()
                i += 1
                j -= 1
        # 初始化新节点，保存归并结果
        dummy = ListNode(-sys.maxsize)
        head = dummy
        listsLen = len(lists)
        # 使用外排序进行归并，若其中某路已归并完，则构造新的败者树
        while listsLen > 0 and listsLen:
            # 初始化败者树
            loserTree = [listsLen] * listsLen
            lists.append(ListNode(-sys.maxsize))
            for i in range(listsLen):
                self.adjust(i, listsLen, lists, loserTree)
            # k-归并，将每次胜者添加到链表的尾部，并读取下一个数，并更新败者树
            while lists[loserTree[0]] != None:
                pos = loserTree[0]
                dummy.next = lists[pos]
                dummy = dummy.next
                lists[pos] = lists[pos].next
                # 如果某一路归并完毕，则需要移除这一路
                if lists[pos] == None:
                    break
                # 更新败者树
                self.adjust(pos, listsLen, lists, loserTree)
            # 去掉归并完的路
            while None in lists:
                lists.remove(None)
                listsLen -= 1
        return head.next
