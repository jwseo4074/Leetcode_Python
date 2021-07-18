# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

# s = "dvdf"
#
# #중복문자가 없어야 한다.
#
# list1 = []
# answer = []
# cnt = 0
# i = 0
#
# while i != len(s):
#     if s[i] not in list1:
#         list1.append(s[i])
#         cnt += 1
#     else:
#         list1.clear()
#         i -= 1
#         cnt = 0
#         continue
#     answer.append(cnt)
#     print(s[i], list1, i, cnt)
#     i += 1
# return max(answer)

# => 타임초과


s = "abcabcbb"
ans = 0
left_cursor = 0
used = {}

for right_cursor, char in enumerate(s):
    print("right_cursor: ", right_cursor, "/ character is: ", char)

    if char in used and left_cursor <= used[char]:
        # 이미 나왔던 문자라면 ?
        left_cursor = used[char] + 1
        # 왼쪽 커서를 반복되는 문자의 다음 문자 인덱스에 + 1
        # abcda 이면 반복되는게 a 니까 길이는 그전에 a로 부터 시작했을거 아니야 이 때 left 는 0 이였겠지
        # left 를 0에서 1을 더해줘 그럼 뭐냐
        # left를 (시작점) 반복되는 문자의 바로 다음 문자의 인덱스로 정해준다.

    else:
        # 처음 나오는 문자라면
        ans = max(ans, right_cursor - left_cursor + 1)
        # 중복 전까지 다른 문자가 연속된 최대 횟수
        # 오른쪽 - 왼쪽 + 1 => 그 사이에 몇개가 있나 ?
    used[char] = right_cursor
    # value값 업데이트
    # 중복됐던거는 그거의 인덱스를 다시 저장
    # abcabc 에서 두번째 a 가 나왔을 때 used[a] = 3 으로 업데이트

    print("left_cursor: ", left_cursor)
    print("answer: ", ans)
    print("used dictionary is: ", used)
    print("\n")
    # return ans

