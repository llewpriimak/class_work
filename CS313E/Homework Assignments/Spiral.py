#python3 Spiral.py < spiral.in
import sys



#This function is designed to add numbers in the left direction

def go_left(my_array, last_digit, n, up1):

  row_indx = up1 # need to increase by 1 with each iteration
  colm_indx = -1

  for num in range(n - 1):

    if my_array[row_indx][colm_indx] == 0:
      my_array[row_indx][colm_indx] = last_digit
      colm_indx = colm_indx - 1
      last_digit = last_digit - 1
    else:
      colm_indx -= 1

  # Add if statement for if the values arent 0
  return my_array, last_digit


###
#This function is designed to add numbers in the down direction
def go_down(my_array, last_digit, n, up1):
  row_indx = 0
  colm_indx = up1   #Need to increase by one with each iteration
  for num in range(n):
    if my_array[row_indx][colm_indx] == 0:
      my_array[row_indx][colm_indx] = last_digit
      last_digit = last_digit - 1
      row_indx += 1
    else:
      row_indx += 1

  return my_array, last_digit

#This function is designed to add numbers in the right direction
def go_right(my_array, last_digit, n, down1):
  row_indx = n - down1    #Need to go down by one with each iteration
  colm_indx = 0
  for num in range(n):
    if my_array[row_indx][colm_indx] == 0:
      my_array[row_indx][colm_indx] = last_digit
      last_digit = last_digit - 1
      colm_indx += 1

    else:
      colm_indx += 1
  return my_array, last_digit

#This function is designed to add numbers in the up direction
def go_up(my_array, last_digit, n, down1):
  row_indx = n - 1
  colm_indx = n - down1   #Needs to go down by one with each iteration
  for num in range(n):
    if my_array[row_indx][colm_indx] == 0:
      my_array[row_indx][colm_indx] = last_digit
      last_digit -= 1
      row_indx -= 1

    else:
      row_indx -= 1

  return my_array, last_digit


def create_spiral(n):
  last_digit = n ** 2
  my_array = []
  for i in range(n):
      single_row = []
      for j in range(n):
          single_row.append(0)
      my_array.append(single_row)
  up1 = 0
  down1 = 1
  while last_digit > 0:
    my_array, last_digit = go_left(my_array, last_digit, n, up1)
    my_array, last_digit = go_down(my_array, last_digit, n, up1)
    my_array, last_digit = go_right(my_array, last_digit, n, down1)
    my_array, last_digit = go_up(my_array, last_digit, n, down1)
    up1 += 1
    down1 += 1

  print(my_array)
  print(last_digit)

# Input: Spiral and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
  i = 0
  for i in range(len(spiral)):
    for j in range(spiral[i]):
      if spiral[i][j] == n:
        num_location = spiral.index(n)
        i+=1
        j+=1

def main():

  data = sys.stdin.read()
  print(data)
  data_list = data.split("\n")

  spiral_dimensions = (int(data_list[0]))
  spiral = create_spiral(spiral_dimensions)
  list_index = 1
  for num in len(data_list):
    print(sum_adjacent_numbers(spiral, int(data_list[list_index])))
    list_index += 1


# read the input file
#
# create the spiral
#
# add the adjacent numbers
#
# print the result

if __name__ == "__main__":
    main()





# TEST ENVIRONMENT##############

# create_spiral(11)
# def boundary_conditions():



