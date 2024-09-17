def string_match(a, b):
  if len(a) < len(b):
    end = len(a)
  else:
    end = len(b)
  count = 0
  for i in range(end-1):
    if a[i] == b[i]:
      if a[i+1] == b[i+1]:
        count+=1
  return count
