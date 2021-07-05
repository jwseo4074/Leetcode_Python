#class Solution:
#   def longestPalindrome(self, s: str) -> str:

s = "123454321"

def expand(left : int , right : int) -> str :
    while left >=0 and right < len(s) and s[left] == s[right] :
        left -= 1
        right += 1
    #print(s[left + 1:right])
    return(s[left + 1:right])

if len(s) < 2 or s == s[::-1]:
    # 예외처리
    # 혹시 모를 예시에 대한 시간 단축
    #return s
    print(s)

result = ""

for i in range(len(s)-1):
    # 인덱스를 조회하는거니깐 마지막은 len -1 임에 주의
    result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

#return result
print(result)