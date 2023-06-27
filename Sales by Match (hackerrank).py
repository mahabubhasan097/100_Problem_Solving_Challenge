def sockMerchant(n, ar):
  socks_count={}
  pairs = 0
  for s in ar:
    socks_count[s] = socks_count.get(s, 0) + 1
  for socks_number in socks_count.values():
    if socks_number == 1:
      continue
    elif socks_number % 2 == 0:
      pairs += (socks_number / 2)
    else:
      pairs += ((socks_number - 1) / 2)
  return int(pairs)      

ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9, ar))