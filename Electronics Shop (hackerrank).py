def getMoneySpent(keyboards, drives, b):
  total_cost = -1
  for i in keyboards:
    for j in drives:
      if total_cost <= i + j and b >= (i + j):
        total_cost = i + j 
      else:
        continue
  return total_cost        

keyboards= [3,1]
drives = [5,2,8]
print(getMoneySpent(keyboards, drives, 10))