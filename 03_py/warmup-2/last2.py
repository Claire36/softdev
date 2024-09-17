def last2(str):
  string = str[-2:]
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == string:
      count+=1
  return count
