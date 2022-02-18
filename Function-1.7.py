from concurrent.futures.process import _threads_wakeups


def has_33(nums):
    for i in range(len(nums)):
        if nums[i] and nums[i + 1] == 3:
            return True
        else: 
            return False

nums = list(map(int, input().split()))
print(has_33(nums))



#has_33([1, 3, 3]) 
#has_33([1, 3, 1, 3]) 
#has_33([3, 1, 3]) 