
def calculateStats(numbers):
   dic = {"avg" : 0, "max" : 0, "min" : 0}
  if len(numbers) != 0:
    num_sum = sum(numbers)
    dic["avg"] = num_sum / len(numbers)
    dic["max"] = max(numbers)
    dic["min"] = min(numbers)
  else:
    print("Input is empty")
  return dic
