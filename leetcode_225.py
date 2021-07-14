import collections

# queue 를 이용한 stack 구현
# deque 는 양쪽에서 접근이 가능하다.

"""
보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.
즉, 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.
"""
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # queue 는 FIFO 라서, 들어간 순서대로 위로 쌓이는데 ,
        # stack 은 제일 나중에 들어간게 처음 나오기 때문에
        # push ( append ) 하면 젤 위에 쌓이게 됨
        # 이거 순서 바꿔줘야 함
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())


    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

stack  = MyStack()
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
print(stack.empty())
