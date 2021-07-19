# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:

digits = "23"
answer = []
table = { "2" : "abc" , "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
index = 0
path = ""

def dfs(index, path):
    if len(digits) == len(path):
        #print(path)
        answer.append([path])
        return

    for i in range(index, len(digits)):
        for char in table[digits[i]]:
            dfs(i + 1, path + char)

#예외 처리
if len(digits) == 0:
    print("예외")
    #return []

dfs(0,"")

#return answer