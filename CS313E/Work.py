import sys
import time


#This function will tell you how many times this can be executed before chris falls asleep
def not_asleep(v, k):
    num_lines = 0
    x = 0
    function = v
    while function >= 1:
      # num_lines += function
      x += 1
      function = v // (k ** x)
    return (x +1)

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  function = v
  total = 0
  for i in range(1, not_asleep(v, k)):
    total += function
    function = v // (k ** i)
  return total


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
# The list to be searched is when the v makes total lines = n
def linear_search (n, k):

  lines_needed = n
  v = 1
  while lines_needed > sum_series(v, k):
    v += 1
  return v


linear_search(100, 5)
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):

  bot = 1
  top = n
  mid = (bot + top) // 2
  total = sum_series(mid, k)
  if k > n:
    return n
  while n != total:
    if total > n and (sum_series(mid - 1, k)) < n:
      break
    elif n < total:
      top = mid
    elif n > total:
      bot = mid
    mid = (bot + top) // 2
    total = sum_series(mid, k)
  return mid



def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
