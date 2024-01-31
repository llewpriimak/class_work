# File: images.py
#
# Description: Read in a plain pgm format file and apply an image
# filter to it selected by the user. Write out the new image to a pgm
# file. The program assumes files are encoded with the plain pgm
# format per http://netpbm.sourceforge.net/doc/pgm.html.
#
# Assignment Number: 11
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.
import os


# I unfortunately ran out of time to write this program.
# The first two functions work but the other two did not.
# it has been a busy week :(


def main():


    """Process one file based on user input.

    1. Get the name of the image file from the user.
    2. Read in the data from the file.
    3. Determine what filter to apply.
    4. Apply the filter.
    5. Write out the new file.
    We assume the user correctly enters the name of a file
    formatted in the plain pgm format"""
    infile_name = input('Enter file name: ')
    # Calls read pgm
    image_raster, max_value = read_pgm_file(infile_name)
    # Calls get_filter_choice
    choice = get_filter_choice()
    if choice == 1:
        result = invert_colors(image_raster, max_value)
    else:
        choices = [mirror, blur, brighten]
        result = choices[choice - 2](image_raster)
    print_result(result)
    save_result(infile_name, max_value, result)


def get_filter_choice():


    """Ask user for which filet to apply to the current image."""
    print('OPTIONS FOR IMAGE FILTER TO APPLY:')
    print('1. Invert colors of image.')
    print('2. Get a mirror image.')
    print('3. Blur image.')
    print('4. Brighten image.')
    return int(input('Please enter your choice: '))


def read_pgm_file(infile_name):


    """Read in the file specified by the given file name.

    We assume infile_name refers to a file in the current working
    directory and that the file is in the plain pgm format.
    Return an image raster (list of lists) with the values from the
    file. Each row is a list in the returned value. Also return
    the max value as specified by the file."""

    with open(infile_name, 'r') as infile:
        magic_num = infile.readline().strip()
        if magic_num != 'P2':
            print('First line of file not magic num P2. '
                  'Instead it is:', magic_num, 'Logic errors may occur')
        second_line = infile.readline().strip()
        if second_line[0] == '#':
            print('in file contains comment:', second_line, '. Discarding.')
            second_line = infile.readline().strip()
        dimensions = second_line.split()
        max_val = int(infile.readline().strip())
        return read_raster(dimensions, infile), max_val


def read_raster(dimensions, infile):


    """Read in and return a list of lists for the values of the image.

    dimensions is a string with 2 ints, the height and width of the
    image. infile is the inout file. We assume the file cursor is
    positioned just before the first data value after the dimensions.
    Return the raster, a list of lists.
    """
    cols, rows = int(dimensions[0]), int(dimensions[1])
    result = [[0 for c in range(cols)] for r in range(rows)]
    row = 0
    current_data = infile.readline().strip().split()
    current_pos = 0
    while row < rows:
        col = 0
        while col < cols:
            if current_pos == len(current_data):
                # Used up the last line, need to read the next line.
                current_data = infile.readline().strip().split()
                current_pos = 0
            result[row][col] = int(current_data[current_pos])
            current_pos += 1
            col += 1
        row += 1
    return result


def print_result(raster):


    """Print the given raster to standard output."""
    for row in range(len(raster)):
        print('Row ', row, ": ", raster[row], sep='')


def save_result(original_name, max_value, raster):


    """Save the raster to a plain pgm file.

    raster is a list of lists of ints representing a grayscale image
    in the plain pgm format. Write out the raster to a plain pgm file.
    Each row is placed on a single line.
    The file name is the original file name before the prefix
    with _alt and then .pgm.
    """
    name = original_name.split('.')[0]
    name += '_alt.pgm'
    with open(name, 'w') as outfile:
        outfile.write('P2\n')
        rows, cols = get_dimensions(raster)
        outfile.write(str(cols) + ' ' + str(rows) + '\n')
        outfile.write(str(max_value))
        outfile.write('\n')
        for row in raster:
            output_row = ''
            for value in row:
                output_row += str(value) + ' '
            output_row = output_row.strip() + '\n'
            outfile.write(output_row)


def invert_colors(raster, maxi):


    """Create and return an inverted version of the raster.

    raster is a rectangular list of lists of ints.
    All values are between 0 and max inclusive. [0, max]
    The returned value has each value altered to max - original_val.

    Simple example, given max is initially 31
     1  2  3  4  5
     6  7  8  9 10
    11 12 13 14 15
    16 17 18 19 20

    would return:
    30 29 28 27 26
    25 24 23 22 21
    20 19 18 17 16
    15 14 13 12 11
    """
    row_check = 0
    for rows in raster:

        for columns in range(len(rows)):
            raster[row_check][columns] = maxi - raster[row_check][columns]

        row_check += 1

    return raster


def mirror(raster):


    """Create a mirror image of the raster.

    Raster is a rectangular list of lists of ints representing an image.

    Simple example:
     1  2  3  4  5
     6  7  8  9 10
    11 12 13 14 15
    16 17 18 19 20

    would return:
     5  4  3  2  1
    10  9  8  7  6
    15 14 13 12 11
    20 19 18 17 16
    """
    for rows in raster:
        rows.reverse()


    return raster




def blur(raster):


    """Create a blurred version of the raster.

    Raster is a rectangular list of lists of ints representing an image.
    Each value in the returned result is the average of a cell and its
    8 neighboring cells. Corner cells only have 3 neighbors and edge
    cells not on the corner have 5 neighbors.
    """
    row_check = 0
    for rows in raster:

        for columns in range(len(rows) - 1):
            get_point = raster[row_check][columns]
            get_point_index = rows.index(get_point)
            total_neighbors = num_neighbors(len(rows), columns, raster)
            print(total_neighbors)
            if total_neighbors == 3:

                get_average = average(raster, row_check, get_point_index, rows, total_neighbors)
                raster[row_check][columns] = get_average

            elif total_neighbors == 5:
                get_average = average(raster, row_check, get_point_index, rows, total_neighbors)
                raster[row_check][columns] = get_average

            else:
                get_average = average(raster, row_check, get_point_index, rows, total_neighbors)
                raster[row_check][columns] = get_average

        row_check += 1


 # def num_neighbors(rows, cols, raster):


    #  Mikes get neighbor function. Placeholder to find neighbors
    # num_neighbors = 0
    # for r in range(rows - 1, rows + 2):
    #     for c in range(cols - 1, cols + 2):
    #         if inbounds(r, c, raster) and raster[r][c]:
    #             num_neighbors += 1
    # if raster[rows - 1][cols - 1]:
    #     num_neighbors -= 1
    # return num_neighbors


# def inbounds(r, c, raster):


    # checks to see if rows and columns value are true
    # Mikes inbounds function
    # return 0 <= r < len(raster) and 0 <= c < len(raster[r])


def average(raster, row_check, get_point_index, rows, neighbors):


        # This will set the average of the surrounding values

        upper_row = raster[row_check - 1]
        lower_row = raster[row_check + 1]
        upper_sum = sum(upper_row[(get_point_index - 1) : (get_point_index + 1)])
        lower_sum = sum(lower_row[(get_point_index - 1) : (get_point_index + 1)])
        get_point_sum = (rows[get_point_index - 1]) + (rows[get_point_index + 1])
        get_average = (upper_sum + lower_sum + get_point_sum) // neighbors

        return get_average



def brighten(raster):


    """Create a brightened version of the raster.

    Raster is a rectangular list of lists of ints representing an image.
    Each value in the returned result is the maximum value of a cell
    and its 8 neighboring cells. Corner cells only have 3 neighbors
    and edge cells not on the corner have 5 neighbors.
    """

    row_check = 0
    for rows in raster:

        for columns in range(len(rows) - 1):
            get_point = raster[row_check][columns]
            get_point_index = rows.index(get_point)
            total_neighbors = num_neighbors(len(rows), columns, raster)

            if total_neighbors == 3:
                pass
            elif total_neighbors == 5:
                pass
            else:
                pass



def get_dimensions(raster):


    rows = len(raster)
    columns = len(raster[0])

    return rows, columns


main()
