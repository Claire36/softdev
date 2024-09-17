def reverse3(nums):
  res = []
  for i in range(len(nums)):
    res.append(nums[len(nums)-1-i])
  return res
