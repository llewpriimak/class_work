# File: first_digit.py
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Number: 12
#
# Name: Llewnosuke Priimak
# EID:  lp27636
# Email: lpriimak@utexas.edu
# Grader: Yugam
#
# On my honor, Llewnosuke Priimak, this programming assignment is my own work
# and I have not provided this code to any other student.

import os


def main():


    """Determine leading digit data for a given file.

    Ask user for file name.
    Expected format is:
    <Explanation of Data>
    <Data source, typically a URL>
    <value 1>,<label 1>
    <value 2>,<label 2>
    ...
    <value N>,<label N>
    Each data line has a single comma. No spaces between the data value
    and the label.
    Determine and print the percentage of values in a data set with a given
    leading digit, [1, 9]. Any values equal to 0 are ignored.
    Also display the max value(s).
    """
    # Main function finds the path to file and calls the other
    # function to process data
    print('Determine percentage of leading digits 1 through 9.')
    file_name = input('Enter file name: ')

    if os.path.isfile(file_name):
        process_file(file_name)
    else:
        path = os.path.dirname(os.getcwd())
        print('Cannot find the file name', file_name, '.')
        print('Please ensure the file is placed in this directory:', path)


def process_file(file_name):


    """Process the given file for first digit information.

    Read the description and then create a map with first digit information.
    """

    """
    I have no idea what the point of this function is. I was able to complete this program
    with every function having less than 25 lines of code. The function read_file() asks for 
    the exact same thing that this function asks for.
    The wording of what this function is supposed to do made it more 
    confusing because it asked to create another map. It didn't make sense to make another dictionary/map. 
    I kept this function here to leave this comment.
    """

    with open(file_name, 'r') as get_file:

        read_data(get_file)


def get_first_num(line_check):


    # This function will return the first number of the integer
    split_line = line_check.split(',')
    max_val_check = int(split_line[0])
    max_val_label = (split_line[1])
    num_len = len(split_line[0])
    num_value = int(split_line[0])
    get_decimal = num_value / (10 ** (num_len - 1))
    str_again = str(get_decimal)
    iso_value = str_again.split('.')
    first_digit = int(iso_value[0])

    return first_digit, max_val_check, max_val_label


def read_data(data_file):


    """
    Returns the first digit dictionary, the max data value, and the label
    for the max data value.
    """
    frequencies = dict.fromkeys(range(1, 10), 0)

    total_digits = 0
    new_max_val = 0
    max_label = ''
    info_line = data_file.readline().strip()
    data_file.readline().strip()
    line_check = data_file.readline().strip()

    # While loop will scan through the data file.
    while line_check != '':

        first_digit, max_val, max_val_label = get_first_num(line_check)

        if max_val > new_max_val:
            new_max_val = max_val
            max_label = max_val_label

        if first_digit != 0:
            frequencies[first_digit] += 1
            total_digits += 1
        line_check = data_file.readline().strip()

    for key in frequencies:
        frequencies[key] = (frequencies[key] / total_digits) * 100

    display_results(info_line, frequencies, new_max_val, max_label)


def display_results(data_description, digit_dictionary, max_value,
                    max_description):


    """ Display the results from the file.

    The assignment handout specifies how to display the information.
    """
    print(f'First digit data for {data_description}:')
    print('Digit Percentage')

    for key in digit_dictionary:
        print(f'{key}    {digit_dictionary[key]:5.1f}')

    print()
    print(f'Max value: {max_value}')
    print(f'Max label: {max_description}')


main()


# Analysis. Answer the questions from the assignment here.
# Be sure these are a comment so the program still runs.

# Question 1.
""" 
Plane crash fatalities and airline from 2013 to 2022
http://www.planecrashinfo.com/database.htm
132,China Eastern Airlines
22,Tara Air
8,Meridian
62,Sriwijaya Air
10,South Sudan Supreme Airlines
5,Soloy helicopters
11,Nigerian Air Force
12,Myanmar Air Force
50,Philippine Air Force
28,Kamchatka Aviation Enterprise
4,Aeroservice/SiLA
4,Med Jet
18,Sudanese Air Force
176,Ukraine International Airlines
3,Pegasus Airlines
8,Lion Air Inc.
97,Pakistan International Airline
20,Air India Express 
7,South West Aviaiton
26,Ukraine Air Force
15,Saha Air
3,Atlas Air Serving Amazon
14,Laser Aereo Colombia
157,Ethiopian Airlines
6,Archipelagos Service Aereos
13,TVPX Aircraft Solutions
41,Aeroflot Russian International Airlines
13,Indian Air Force
5,Pakistan Army
2,Private
5,Ukraine Air Alliance
19,Busy Bee Congo
12,Bek Air
12,People Liberation Army Air Force
3,Papillon
71,Saratov Airlines
66,Iran Aseman Airlines
39,Russian Air Force
5,Liberty Helicopters
11,Mc Aviation
51,Bangla Airlines
257,Algerian Air Force
1,Southwest Airlines
9,US Air Force
112,Cubana
10,Fly SAX
1,Rovos Air
20,Ju Air
15,Russian Air Force
1,Air Niugini
189,Lion Air
1,Fly Jamaica Airways
4,My Cargo Airlines
5,Australian Corporate Jet
7,Swan Aviation
6,ETA Air Charter
2,Air Cargo Carriers
2,Summit Air
122,Myanmar Air Force
3,Angel Flight
16,USMC
12,Air Force of the Democratic Republic of the Congo
7,Guicango
4,Valan International Cargo Charter
11,Costal Aviation
1,West Wind Aviation
12,Naure Air
2,West Air Sweden
1,Daallo Airlines
23,Tara Air
2,Kasthamandap Airlines
3,True Aviation Ltd.
22,Ecuador Army
62,Flydubai
7,Marquise Aviation Corp.
5,Smoky Mountain Helicopters
12,Sunbird Aviation
13,CHC Helikopter Service
66,Egypt Air
29,Indian Air Force
16,Heart of Texas Hot Air Balloon Rides
5,Hageland Aviiation
5,AE Aviation
71,LAMIA Bolivia
13,Indonesian Police
48,Pakistan International Airlines
13,Indonesian Air Force
5,Aerosucre Colombia
92,Russian Air Force
37,Syrian Air Force
43,Transaia
10,Private
150,Germanwings
9,Promech Air
122,Indonesian Air Force
11,Colombia Air Force
1,Komala Air
54,Trigana Air Service
7,Senegalair
3,Rainbow King Lodge
11,U.S. Army
10,Avistar Mandari
4,Trigana Air Service
224,Metrojet
41,Allied Services Limited
7,Alpine Adventures
15,Turuhan Avia
2,Scoala Superioara de Aviatie Civla
76,Algerian Air Force
18,Nepal Airlines
11,Libyan Air Cargo
239,Malaysia Airlines
2,Helicopters Inc/KOMO TV
8,Lineas Aéreas Comerciales
8,Suomen Urheiluilmailijat
6,Alisansa Colombia
16,Laos Air Force
49,Ukraine Air Force
4,Skyward International Aviation
18,Vietnam People's Army Air Force
298,Malaysia Airlines
45,TransAsia Airways
116,Air Algérie
39,Sepahan Airlines
7,Ukraine Air Alliance
3,Safari Express Cargo
4,Hevlift
2,Air Evac Lifeteam
6,Air Sirin
162,AirAsia
3,Med-Trans Corporaion
6,Transaereo 5074
21,SCAT Air
5,South Airlines
7,Compagnie Africaine d' Aviation
2,Ace Air Cargo
7,National Air Cargo
4,Ornge Air Ambulance
20,Indian Air Force
3,Asiana Airlines
10,Rediske Air
4,Ethiopian Air Force
2,United Parcel Service
16,Associated Aviation
2,MASwings
49,Lao Airlines
8,Aerocon
13,Indonesian Army
5,Bearskin Airlines
50,Tarastan Airlilnes
3,Bond Air Services Ltd.
33,Mozambique Airline
5,Heringer taxi Aero
9,IrAvia
 """

#   Question 2:
"""
1: 45%
2: 20%
3: 10%
4: 8%
5: 5%
6: 4%
7: 3%
8: 3%
9: 2%
"""

# Question 3:

"""
Results:
1     33.8
2     16.2
3      9.1
4     10.4
5     10.4
6      5.8
7      7.8
8      3.2
9      3.2

Max value: 298
Max label: Malaysia Airlines

I overestimated how much 1 would appear and underestimated how much 4 and 5 would appear.
I am definitely suprised by the results I got.
The actual results are moderately intuitive. This is due to the fact that plane crash fatalities are often in the lower
teens or high 100's. What I didn't completely expect was that most plane fatalities are not actually of commercial airlines
but of private or military. This is why those numbers are slightly different. Yes there are 100%
data sets that would not follow the typical results. It completely depends on what data you are looking at because the 
different sets will give such different data types.

"""
