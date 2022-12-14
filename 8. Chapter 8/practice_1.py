def greatestOfThree(nums):
    if nums[0] > nums[1]:
        if (nums[0] > nums[2]):
            return nums[0]
        else:
            return nums[2]
    elif nums[1] > nums[2]:
        return nums[1]
    return nums[2]


nums = input("Enter three positive integers: ").split()


print(greatestOfThree(list(map(int, nums))))
