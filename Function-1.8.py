def spy_game(nums):
    s = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            s.append(nums[i])
    for j in range(len(s)):
        if s[j] == 0 and s[j+1] == 0 and s[j+2] == 7:
            return True
        else: 
            return False

nums = list(map(int, input().split()))
print(spy_game(nums))