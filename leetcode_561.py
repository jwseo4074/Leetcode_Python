nums = [1,4,3,2]
nums.sort()

sum = 0
answer_list = []
for i in range(0,len(nums)):
    #min_list = []
    #if i % 2 != 0 :
    #    min_list.append(nums[i])
    #    min_list.append(nums[i-1])
    #    answer_list.append(min(min_list))

    # 최적화
    if i % 2  == 0 :
        sum += nums[i]

#sum = 0
#for i in answer_list:
#    sum += i
print(sum)

#파이썬 다운 풀이
#return sum(sorted(nums)[::2])