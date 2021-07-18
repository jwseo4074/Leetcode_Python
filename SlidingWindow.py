def solve_max_sum(arr, k):
    max_sum = float('-inf')
    # 최대값은 마이너스 무한대로 초기화
    start = 0
    # 시작 인덱스 = 0 으로 초기화
    curr_sum = 0
    # 현재까지의 합 0 으로 초기화

    for end, val in enumerate(arr):
        curr_sum += val
        # 현재까지의 합에 val 을 더해줌

        if end - start + 1  == k:
            # 예를 들어 k가 3이라면 3개의 합이니까
            # 오른쪽 마이너스 왼쪽 + 1 했을 때 그 합이 k가 되면 끝남
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            # 현재까지의 합에다가 시작점에꺼 하나 빼줘 그래야 3개가 됨
            # 왜냐면 처음에 curr_sum += val 해서 값 더해준 상태인데 4개의 합을 해놓은 상태니까
            start += 1
            # 시작점 한칸 오른쪽으로 옮겨줘
    return max_sum

arr = [2,3,4,1,5]
k = 3

print(solve_max_sum(arr,k))

