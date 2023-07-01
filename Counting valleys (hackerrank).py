def countingValleys(steps, path):
    count=0
    valley=0
    for i in path:
        count -= 1 if i == "D" else -1     
        valley += 1 if (count==0 and i=="U") else 0
    return valley

print(countingValleys(2, 'DU'))  