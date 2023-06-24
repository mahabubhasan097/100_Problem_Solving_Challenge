def kangaroo(x1, v1, x2, v2):
  if v1 <= v2:
    return "NO"
  while x1 <= x2:
    if x1 == x2:
      return 'YES'
    x1 += v1
    x2 += v2
    if x1 >  x2:
      break
  return 'NO'
print(kangaroo(1113, 612, 1331, 610))