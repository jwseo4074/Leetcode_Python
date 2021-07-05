import re

text = "I like apble And abple"
print(text)
text_mod = re.sub('apble|abple',"apple",text)
print (text_mod)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
words_before = list(paragraph.split())
print(words_before)
words_after = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
print(words_after)