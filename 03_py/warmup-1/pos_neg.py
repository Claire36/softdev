def pos_neg(a, b, negative):
  if negative:
    if (a<0) & (b<0):
      return True
  else:
    if (a<0) & (b>0):
      return True
    if (a>0) & (b<0):
      return True
  return False
