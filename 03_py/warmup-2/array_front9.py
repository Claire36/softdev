def array_front9(nums):
  if (len(nums)<4):
    end = len(nums)
  else:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False
