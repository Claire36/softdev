def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  sum = 0
  for i in range(len(nums)):
    sum+=nums[i]
  sum/=len(nums)
  return sum
