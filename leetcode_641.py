class ListNode:
    def __init__(self, val, right=None, left=None):
        self.right = right
        self.left = left
        self.val = val


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.tail = ListNode(None)
        self.head = ListNode(None)  # dummy node
        self.k = k  # deque의 max length 지정
        self.len = 0  # 현재 deque 속 원소의 개수
        self.head.right = self.tail  # head -> tail 연결 (doubly linked list)
        self.tail.left = self.head  # head <- tail 연결 (doubly linked list)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            new_node = ListNode(value)  # 삽입할 노드 생성
            n = self.head.right  # head 다음의 노드를 따로 저장 (본래 head <-> head_next)
            self.head.right = new_node
            n.left = new_node  # head->new_node & new_node <- head_next
            new_node.left = self.head
            new_node.right = n  # head<-new_node & new_node -> head_next
            self.len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            new_node = ListNode(value)  # 삽입할 노드 생성
            n = self.tail.left  # tail 다음의 노드를 따로 저장 (본래 tail_before <-> tail)
            self.tail.left = new_node
            n.right = new_node  # tail_before -> new_node & new_node <- tail
            new_node.left = n
            new_node.right = self.tail  # tail_before <- new_node & new_node -> tail
            self.len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            head_right = self.head.right.right  # head <-> head.right <-> head.right.right
            head_right.left, self.head.right = self.head, head_right  # head <-> head.right.right
            self.len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            tail_before = self.tail.left.left  # tail.left.left <-> tail.left <-> tail
            tail_before.right, self.tail.left = self.tail, tail_before  # tail.left.left <-> tail
            self.len -= 1
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.head.right.val  # head <-> head.right

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.tail.left.val # tail.left <-> tail

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k
    # def __init__(self, k: int):
    #     self.head = ListNode(None)
    #     self.tail = ListNode(None)
    #     self.k = k
    #     self.len = 0
    #     self.head.right = self.tail
    #     self.tail.left = self.head
    # # ->  head  ->  tail ->
    # # <-        <-
    #
    # def _add(self, node: ListNode, new: ListNode):
    #     n = node.right
    #     node.right = new
    #     new.left = node
    #     new.right = n
    #     n.left  = new
    #     # node -> new -> n
    #     #      <-     <-
    #     # 이렇게 중간에 new 끼워넣는 형식
    #
    # def _del(self, node: ListNode):
    #     n = node.right.right
    #     node.right = n
    #     node.left = node
    # # node 바로 오른쪽꺼 지우는 작업
    #
    # def insertFront(self, value: int) -> bool:
    #     if self.len == self.k:
    #         return False
    #     self.len += 1
    #     self._add(self.head,ListNode(value))
    #     return True
    #
    # def insertLast(self, value: int) -> bool:
    #     if self.len == self.k:
    #         return False
    #     self.len += 1
    #     self._add(self.tail,ListNode(value))
    #     return True
    #
    # def deleteFront(self) -> bool:
    #     if self.len == 0:
    #         return False
    #     self.len -= 1
    #     self._del(self.head)
    #     return True
    #
    # def deleteLast(self) -> bool:
    #     if self.len == 0:
    #         return False
    #     self.len -= 1
    #     self._del(self.tail)
    #     return True
    #
    # def getFront(self) -> int:
    #     return self.head.right.val if self.len else -1
    #
    # def getRear(self) -> int:
    #     return self.tail.left.val if self.len else -1
    #
    # def isEmpty(self) -> bool:
    #     return self.len == 0
    #
    # def isFull(self) -> bool:
    #     return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
