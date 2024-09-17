def near_hundred(n):
  if abs(100-n) <= 10:
    return True
  if abs(200-n) <= 10:
    return True
  return False
