import collections

"""
zip 함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는
새로운 튜플 시퀀스를 만드는 역할을 한다.
먼저 다음과 같이 a,b,c 리스트를 각각 정의하고
zip(a, b) 를 실행한 결과를 보자
"""

a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]
print(list(zip(a,b)))
print(list(zip(a,b,c)))

print()

nums = [1,1,1,2,2,3]
k = 2

freqs = collections.Counter(nums)
print(freqs)
# 카운터 함수 잘 이해해두기

print()

# 파이썬의 2가지 기능 = zip 과 * , collection 파일에서 다시 소개
print(*collections.Counter(nums).most_common(k))
# k가 2이므로 제일 많이 나오는거 2개
# 1이 세번, 2가 2번
print(list(zip(*collections.Counter(nums).most_common(k))))
# 앞에꺼만 떼와서 zip 으로 묶어줌
print(list(zip(*collections.Counter(nums).most_common(k)))[0])
# 묶어준거에서 첫번째 인덱스
print(list(zip(*collections.Counter(nums).most_common(k)))[1])

print()

"""
아스테리스크 ( * )
언패킹의 개념 ( 풀어 헤친다. )
"""

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits)
# 만약 각 요소의 값만 출력하고 싶으면 ?
print(fruits[0],fruits[1],fruits[2],fruits[3])
# 이게 아니면 ? for 문으로 돌 수도 있음

# 이때 언패킹을 해준다면 쉽게 표현 가능
print(*fruits)

print()

# 또한 변수의 할당도 아스테리스크를 활용가능하다.
a, *b = [1,2,3,4]
print(a)
print(b)

print()

*a ,b = [1,2,3,4]
print(a)
print(b)

"""
변수의 할당 또한 이렇게 *로 묶어서 처리가능하다.
일반적인 변수는 값을 하나만 취하지만 *로 처리하게 되면 나머지 모든 값을 취하게 된다.
이외에도 활용 방법은 상당히 많다.
*는 파이썬에서 매우 중요하며 자주 쓰이므로 반드시 숙지하자.

마지막으로 하나가 아닌 2개를 쓰는 경우도 있다.

* 한개는 튜플 또는 리스트 등의 시퀀스 언패킹이고, ** 2개는 다음과 같이 키/값 페어를 언패킹하는 데 사용된다.
"""

date_info = {'year' : '2020', 'month' : '01', 'day' : '7'}
print(date_info)

print()

new_info = {**date_info, 'day' : '14'}
print(new_info)
# 이처럼 **date_info에 모든 요소를 언패킹할 수 있으며, 여기서는 'day'를 업데이트까지 했다.
# 바뀐 값도 적용된다.
