
#  File: TestBinaryTree.py

#  Description: This is a binary search tree that can return various information

#  Student Name: Llewnosuke Priimak

#  Student UT EID: lp27636

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number:52020

#  Date Created:03/22/23

#  Date Last Modified:03/22/23


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print('  ' * 3 * level + '----->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return


    # Num_nodes_helper will return the number of nodes in
    # the BST
    def num_nodes_helper(self, aNode):
        if aNode is not None:
            return 1 + Tree.num_nodes_helper(self, aNode.lChild) + Tree.num_nodes_helper(self, aNode.rChild)
        else:
            return 0


    #Returns the Min val in the BST
    def min_helper(self, aNode):

        if aNode.lChild is None:
            return aNode.data
        else:
            return Tree.min_helper(self, aNode.lChild)


    # Returns the max val in the BST
    def max_helper(self, aNode):

        if aNode.rChild is None:
            return aNode.data
        else:
            return Tree.max_helper(self, aNode.rChild)


    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):

        # Check for edge cases
        if Tree.num_nodes_helper(self, self.root) == 1:
            return 0
        elif Tree.num_nodes_helper(self, self.root) == 0:
            return 'Range is undefined'
        else:
            return Tree.max_helper(self, self.root) - Tree.min_helper(self, self.root)


    # Helps create the list of nodes at a level
    def level_helper(self, aNode, node_list, level):


        if level != 0:
            if aNode is not None:
                Tree.level_helper(self, aNode.lChild, node_list, level - 1)
                Tree.level_helper(self, aNode.rChild, node_list, level - 1)
                return node_list
            else:
                return node_list
        else:
            if aNode is not None:
                node_list.append(aNode.data)
            else:
                return node_list


    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if self.root is None:
            return []
        if level == 0:
            return [self.root.data]
        elif Tree.get_height(self) < level + 1:
            return []
        else:
            node_list = []
            Tree.level_helper(self, self.root, node_list, level)
            return node_list


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):

        node_list = []

        height = Tree.get_height(self)
        if height == 1:
            return [self.root]
        for i in range(height):
            node_list.append(Tree.get_level(self, i)[0])

        return node_list


    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_helper(self, aNode):

        if aNode is not None:
            if aNode.lChild is None and aNode.rChild is None:
                return aNode.data
            else:
                return Tree.sum_leaf_helper(self, aNode.lChild) + Tree.sum_leaf_helper(self, aNode.rChild)
        return 0


    # The sum_leaf_nodes here is a little confusing on whether or not i can modifiy
    # the parameters of the function so I just wrote the helper function
    # to do all the work. If I can modify the parameters of sum_leaf_nodes it
    # will be the same as above
    def sum_leaf_nodes(self):
        return Tree.sum_leaf_helper(self, self.root)


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())


    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())



    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())


    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()



