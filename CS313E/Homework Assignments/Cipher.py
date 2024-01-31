#  File: Cipher.py

#  Student Name: Luke Charpentier

#  Student UT EID: lhc567

#  Partner Name: Llewnosuke Priimak

#  Partner UT EID: lp27636

#  Course Name: CS 313E

#  Unique Number: 52020

#  Date Created: 29 Jan 2023

#  Date Last Modified: 31 Jan 2023
import math
import sys

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt ( strng ):

  for x in range(len(strng)):
    for y in range(-1, -(len(strng) + 1), -1):
      if strng[y][x] != '*':
        print(strng[y][x], end='')

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def decrypt ( strng ):

  for x in range(-1, -(len(strng) + 1), -1):
    for y in range(len(strng)):
      if strng[y][x] != '*':
        print(strng[y][x], end='')

def e_string_table(complete_message, size):
    table = [[None] * size for i in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(complete_message):
                table[i][j] = complete_message[k]
                k += 1
            else:
                break
    return table

def d_string_table(complete_message, size):
    table = [[None] * size for i in range(size)]
    k = 0
    for i in range(-1, -(size + 1), -1):
        for j in range(size):
            if k < len(complete_message):
                table[j][i] = complete_message[k]
                k += 1
            else:
                break
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(complete_message):
                if table[i][j] != None:
                    table[i][j] = complete_message[k]
                    k += 1
                else:
                    table[i][j] = '*'
    return table


def e_add_star(message):

  size = math.ceil(math.sqrt(len(message)))
  dots = '*' * (size**2 - len(message))
  complete_message = message + dots
  table = e_string_table(complete_message,size)
  new_table = []
  for row in table:
    new_table.append(row)

  return new_table

def main():

  data = sys.stdin.read()
  inputs = data.split("\n")
  encrypt_sqr = e_add_star(inputs[0])
  decrypt_sqr = d_string_table(inputs[1], math.ceil(math.sqrt(len(inputs[1]))))

  encrypt(encrypt_sqr)
  print('')
  decrypt(decrypt_sqr)

  # read the strings P and Q from standard input

  # encrypt the string P

  # decrypt the string Q

  # print the encrypted string of P
  # and the decrypted string of Q

if __name__ == "__main__":
  main()

