
def calculateStats(numbers):
  avg, max_num, min_num = 0,0,0
  if len(numbers) != 0:
    num_sum = sum(numbers)
    avg = num_sum / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
  else:
    print("Input is empty")
  return avg, max_num, min_num
