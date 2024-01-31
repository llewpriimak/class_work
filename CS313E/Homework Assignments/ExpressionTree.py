#  File: ExpressionTree.py

#  Description: This program takes a string expression, turns it into a BST, and evaluates it

#  Student Name: Llewnosuke Priimak

#  Student UT EID: lp27636

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52020

#  Date Created: 03/19/23

#  Date Last Modified: 03/20/23

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree (object):
    def __init__ (self):
        self.root = None
        self.current = None


    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree (self, expr):

        all_tokens = expr.split()
        stack = Stack()
        self.root = Node()
        self.current = self.root
        while len(all_tokens) != 0:
            token = all_tokens.pop(0)
            if token == '(':
                self.current.lChild = Node()
                stack.push(self.current)
                self.current = self.current.lChild

            elif token in operators:

                self.current.data = token
                stack.push(self.current)
                self.current.rChild = Node()
                self.current = self.current.rChild

            elif token == ')':
                if not(stack.is_empty()):
                    self.current = stack.pop()

            else:
                self.current.data = token
                self.current = stack.pop()


    # This function takes the two child values and returns
    # the evaluation of the two through the operator
    def helper_calculate(self, operate, lChild, rChild):

        if operate == '+':
            return (lChild) + (rChild)
        elif operate == '-':
            return (lChild) - (rChild)
        elif operate == '*':
            return lChild * rChild
        elif operate == '/':
            return lChild / rChild
        elif operate == '//':
            return lChild // rChild
        elif operate == '%':
            return lChild % rChild
        elif operate == '**':
            return lChild ** rChild


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):

        if aNode!= None:
            if not(aNode.lChild.data in operators) and not(aNode.rChild.data in operators):

                return Tree.helper_calculate(self, aNode.data, float(aNode.lChild.data), float(aNode.rChild.data))

            elif aNode.lChild.data in operators and aNode.rChild.data in operators:
                return Tree.helper_calculate(self, aNode.data, Tree.evaluate(self, aNode.lChild), Tree.evaluate(self,aNode.rChild))

            else:
                if aNode.lChild.data in operators:
                    return Tree.helper_calculate(self, aNode.data, Tree.evaluate(self, aNode.lChild),
                                             float(aNode.rChild.data))
                else:
                    return Tree.helper_calculate(self, aNode.data, float(aNode.lChild.data),
                                             Tree.evaluate(self, aNode.rChild))


    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode != None:
                return (f' {aNode.data}{Tree.pre_order(self, aNode.lChild)}{Tree.pre_order(self, aNode.rChild)}')
        return ''


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode != None:
                return (f'{Tree.post_order(self, aNode.lChild)}{Tree.post_order(self, aNode.rChild)} {aNode.data}')
        return ''


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
