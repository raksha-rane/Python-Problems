# Recursive function to reverse a string
def string_reverse(str):
  if len(str) == 0:
    return str
  else:
    return string_reversal(str[1:]) + str[0]
  
  str = "reversal"
  reverse = string_reverse(str)
  print(reverse)
