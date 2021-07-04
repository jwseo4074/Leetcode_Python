import re

paragraph = str(input())
ban = str(input())
banned = []
banned.append(ban)

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

input_list = []
count_list = []

for i in range(len(words)):
    count_list.append(words.count(words[i]))

M = max(count_list)
for i in range(len(count_list)):
    if M == count_list[i]:
        print(words[i])
        break

"""
사이트에 맞는 정답

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        input_list = []
        count_list = []

        for i in range(len(words)):
            count_list.append(words.count(words[i]))

        M = max(count_list)
        for i in range(len(count_list)):
            if M == count_list[i]:
                return words[i]
                
"""