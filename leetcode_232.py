import collections


class MyQueue:
    # push(x)  요소 x 를 큐 마지막에 삽입한다.
    # pop() 큐 처음에 있는 요소를 제거한다.
    # peek 큐 처음에 있는 요소를 조회한다.
    # empty 큐가 비어있는지 여부 리턴

    # 스택을 이용하여 큐를 구현하라.

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            #output 이 비어있으면
            while self.input:
                #input 이 있는 동안에
                self.output.append(self.input.pop())
                #input 에서 마지막 꺼 하나 빼서 output에다가 append
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.output) == 0 and len(self.input) == 0