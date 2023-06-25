def birthday(s, d, m):
  count = 0
  sum_s = 0
  if len(s) == m and s[0] == d and m == 1:
    return 1
  elif m > len(s):
    return 0
  else:
    for n in range(len(s)):
      sum_s = sum(s[n:n+m])
      if sum_s == d:
        count += 1
      else:
        continue
    return count


s=[4]
d=4
m=1
print(birthday(s, d, m))