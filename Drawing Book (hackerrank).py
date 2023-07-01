def pageCount(n, p):
  if abs(0 - p) > abs(n - p):
    if n%2 != 0 and n-p ==1:
      return 0
    elif n%2==0 and p%2 != 0:
      return int(abs(((n-p) + 1)/2))
    elif n%2 != 0 and p%2 == 0:
      return int(abs(((n-p) - 1)/2))
    else:
      return int(abs((n-p)/2))
  else:
    if p%2==0:
      return int(p/2)
    else:
      return int(abs((1-p)/2))         

print(pageCount(5, 3))  