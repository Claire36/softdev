def sum67(nums):
  sum = 0
  skip = False
  for i in range(len(nums)):
    if nums[i] == 6:
      skip = True
    if (nums[i] == 7) & (skip == True):
      skip = False
      sum-=7
    if skip:
      continue
    sum+=nums[i]
  return sum
