def migratoryBirds(arr):
  bird_type_track = {}
  for a in arr:
    bird_type_track[a] = bird_type_track.get(a, 0) + 1
  max_bird_type_sighted = 0
  result = None
  for bird_type, bird_type_sighted in bird_type_track.items():
    if bird_type_sighted > max_bird_type_sighted or (bird_type_sighted == max_bird_type_sighted and bird_type < result):
      max_bird_type_sighted = bird_type_sighted
      result = bird_type

  return result  

arr=[1, 2, 4, 3, 5, 4, 3, 2, 1, 3, 4]
print(migratoryBirds(arr)) 