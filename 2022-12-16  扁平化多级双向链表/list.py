class Solution:
    def flatten(self, head: "Node") -> "Node":
        def dfs(node: "Node") -> "Node":  #按深度优先搜索节点
            cur = node                    #将当前节点用cur来标识
            # 记录链表的最后一个节点
            last = None

            while cur:                   #当前节点存在
                nxt = cur.next           #当前节点的下一节点用nxt来标识
                # 如果有子节点，那么首先处理子节点
                if cur.child:             #当前节点存在子节点
                    child_last = dfs(cur.child)    #深度优先搜索当前节点的子节点

                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child       #插入子节点
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt       #将子节点的末尾与原节点的下一节点相连
                        nxt.prev = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head

class Node:
    def __int__(self,val,prev,next,child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


