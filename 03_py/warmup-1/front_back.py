def front_back(str):
  if len(str) > 2:
    return str[-1] + str[1:(len(str)-1)] + str[0]
  elif len(str) == 2:
    return str[-1] + str[0]
  else:
    return str
