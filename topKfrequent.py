def topKFrequent(nums, k):
    nums_count_d = {}
    top_k_count = [nums[0], nums[1] ]
    for number in nums:
        if number in nums_count_d:
            nums_count_d[number]+=1
        else:
            nums_count_d[number]=1
        if nums_count_d[number] > max(nums_count_d[top_k_count[0]]):
            top_k_count[0] = number
        elif nums_count_d[number] > min(top_k_count):
            top_k_count[1] = number
    return top_k_count

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print topKFrequent(nums, k)
