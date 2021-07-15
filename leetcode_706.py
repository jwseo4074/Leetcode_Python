import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # 키값이 없는걸 조회를하면 자동으로 디폴트 생성하게 해준다.

    def put(self, key: int, value: int) -> None:
        # 보통의 경우 모듈러 연산을 이용해 해싱을 진행함 ( 나머지 )

        index = key % self.size
        # index는 해싱의 키 값이 될것이다.

        if self.table[index].value is None:
            # self.table[index] 가 아니고 self.table[index].value 로 해놓은 이유는 ?
            # self.table 이 collections.defaultdict(ListNode) 이기 때문에
            # 존재하는 인덱스를 조회하면 ? 바로 생성을 해버릴거기 때문
            self.table[index] = ListNode(key, value)
            return

        # 인덱스의 키에 값이 이미 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        # 키에 해당하는 값이 존재하지 않으면 -1 리턴

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        # while 로 연결리스트 따라가다가 결국 못찾으면 loop 빠져 나오면서 -1 리턴

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 값이 있을 경우는 2가지로 나뉘어짐

        # 1. 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            # one line if-else
            # 결과 = A if 조건 else B
            return
        # 2. 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev = p
            p = p.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)