class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []
        for i in range(len(s)):
            if s[i].isalnum():
                answer.append(s[i].lower())

        answer_2 = []
        answer_2 = answer[::-1]

        for i in range(len(answer)):
            if answer[i] != answer_2[i]:
                return False
        return True
