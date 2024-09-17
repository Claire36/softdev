def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    sum = 0
    skip = False
    for i in range(len(nums)):
      if skip:
        skip = False
        continue
      if nums[i] == 13:
        skip = True
        continue
      else:
        sum+=nums[i]
        skip = False
  return sum
