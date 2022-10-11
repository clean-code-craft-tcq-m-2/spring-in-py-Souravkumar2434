
def calculateStats(numbers):
  num_sum = sum(numbers)
  avg = num_sum / len(numbers)
  max_num = max(numbers)
  min_num = min(numbers)
  return avg, max_num, min_num
