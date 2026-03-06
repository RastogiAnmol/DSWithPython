def three_sum_unique_triplets(nums: list[int], target: int) -> list[list[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    
    def two_sum(arr: list[int], goal: int):
        left, right = 0, len(arr)-1
        res = []
        while left < right:
            sum = arr[left] + arr[right]
            if sum == goal:
                res.append([arr[left], arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum > goal:
                right -= 1
            else:
                left += 1
        return res
        
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        tuples = two_sum(nums[i+1:], target-nums[i])
        for pair in tuples:
            result.append([nums[i]] + pair)
    return result

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = three_sum_unique_triplets(nums, target)
    for row in res:
        print(" ".join(map(str, row)))