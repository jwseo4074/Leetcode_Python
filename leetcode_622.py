# 큐는 전형적인 FIFO 자료구조
# 일렬로 줄을 서있는 모습

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        # 최대 길이 = k
        self.front = 0
        # front pointer
        self.rear = 0
        # rear pointer
        # 처음엔 둘다 0으로 설정

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            # q 의 rear 포인터에 값이 None (비어있어야 함)
            self.q[self.rear] = value
            # rear 포인터(처음엔 0)에 값 추가해주고
            self.rear = (self.rear + 1) % self.maxlen
            # k 가 5라면 (최대 길이가 5) => 1 % 5 = 1, rear 포인터 1로 바까주고
            return True

            # 처음에 front에(배열의 인덱스 0 에) value 값 들어가있고
            # rear은 1로 바껴진 상태
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        #첫번째에 (front)에 값이 없다 ? -> 잘못됐다 ( 뺄게 없으니깐 )
        else:
            self.q[self.front] = None
            #front 값 None 으로 바꿔주기
            self.front = (self.front + 1) % self.maxlen
            #front 포인터 1 증가해주기
            return True

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]
    # 인덱스 0에다가 값 넣으면 rear 포인터는 1이 되니까
    # rear 포인터 ( 젤 마지막 ) 꺼를 알고 싶으면 -1 을 해줘야지  ( enqueue 보면 됨 )

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()