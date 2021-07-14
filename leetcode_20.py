#class Solution:
#    def isValid(self, s: str) -> bool:

str = "(){}[]"
#str = "([)]"

stack = []

table = {'{':'}', '[':']', '(':')'}

for char in str:
    if char not in table:
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        # return False
        print(False)
#return len(stack) == 0