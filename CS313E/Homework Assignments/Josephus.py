#  File: Josephus.py

#  Student Name: Llewnosuke Priimak

#  Student UT EID: lp27636

#  Course Name: CS 313E

#  Unique Number: 52020

#  Date Created: March 5 2023

#  Date Last Modified: March 7 2023
import sys

class Link(object):
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.last = None
    self.first = None
    self.total = 0

  # Insert an element (value) in the list
  def insert ( self, data ):
    current = Link(data)
    if self.total == 0: #This is for the first created node
      current.next = current.data
      self.first = current
      self.last = current
    else: # Every node after the first
        current.next = self.last
        self.last = current
    self.first.next = current #Makes the linked list circular
    self.total += 1

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.last
    for i in range(self.total):
      if current.data == data:
        return current.data
      else:
        current = current.next
    return None

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):

    if self.last == None:
      return None
    before = self.first
    current = self.last
    after = self.last.next
    for i in range(self.total):
      if current.data == data:
        self.last = after
        before.next = self.last
        self.total -= 1
        return current
      else:
        before = current
        current = current.next
        after = current.next
    return None

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    before = self.first
    current = self.last
    after = self.last.next
    for i in range(self.total): #This will set the current Node to the Start
      if current.data == start:
        break
      else:
        before = current
        current = current.next
        after = current.next
    for i in range(n - 1): #This will set the current node n spots from the Start
      before = current
      current = current.next
      after = current.next
    deleted = current.data
    next_link = current.next
    if self.total > 1: # Deletes and reconnects the nodes and links
      self.last = after
      before.next = self.last
      self.total -= 1
    return deleted, next_link

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    lst = []
    current = self.last
    for i in range(self.total):
      lst.append(current.data)
      current = current.next
    lst.sort()
    return str(lst)



def main():

  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int(line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int(line)
  circle = CircularList()


  for i in reversed(range(1, num_soldiers + 1)):
    circle.insert(i)
  for i in range(num_soldiers - 1):
    deleted, start_count = circle.delete_after(start_count, elim_num)
    print(deleted)
  print(circle.last.data)


if __name__ == "__main__":
  main()
