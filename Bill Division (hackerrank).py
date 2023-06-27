def bonAppetit(bill, k, b):
  cost = 0
  for i in range(len(bill)):
    if i==k:
      continue
    else:
      cost += bill[i]
  if (cost/2) == b:
    return 'Bon Appetit'
  else:
    return int(abs((cost/2)-b))         

bill=[3, 10, 2, 9]
print(bonAppetit(bill, 1, 12))