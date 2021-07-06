nums = [-1,0,1,2,-1,-4]
# 합이 0이 되게 하는 원소 3개 리스트로 반환
# 브루트 포스면 시간 초과임
# 정렬 된거 => -4 -1 -1 0 1 2
nums.sort()
answer = []
for i in range (len(nums)-2):
    # 중복된 값 건너 뛰기 ? 이게 뭔지 모르겠음
    if i > 0 and nums[i] == nums[i-1]:
        continue

    #간격 좁혀가면서 sum 계산
    left = 0
    right = len(nums)-1

    while left < right :
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
            # 제일 작은거 하나 큰거로
        elif sum > 0:
            right -= 1
            # 제일 큰거 하나 작은거로
        else :
            answer.append([nums[i], nums[left], nums[right]])

            #이거 안하면 어케 댐 ?
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1

print(answer)



