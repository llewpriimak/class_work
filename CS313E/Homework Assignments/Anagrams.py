# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Llewnosuke Priimak

# Student UT EID: lp27636

# Course Name: CS 313E

# Unique Number: 52020

# Output: True or False
def are_anagrams(str1, str2):
    lst1 = []
    lst2 = []
    for i in str1:
        lst1.append(ord(i))
    for i in str2:
        lst2.append(ord(i))
    sum1 = sum(lst1)
    sum2 = sum(lst2)

    return sum1, sum2


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):

    family_lst = []
    for i in range(len(lst)):
        sum1, sum2 = are_anagrams(lst[i],lst[i])
        if sum1 not in family_lst:
            family_lst.append(sum1)
        if sum2 not in family_lst:
            family_lst.append(sum2)

    return len(family_lst)

def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
