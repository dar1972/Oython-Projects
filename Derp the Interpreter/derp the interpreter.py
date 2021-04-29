"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a
symbol table).  It dumps the symbol table, produces the expression infix with
parentheses to denote order of operation, and evaluates/produces the result of
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Dhruv Rajpurohit
"""

from dataclasses import dataclass
from typing import Union

@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str


@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
##############################################################################

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    node = tokens.pop(0)
    if node in ["-", "+", "*", "//"]:
        return MathNode(parse(tokens), node, parse(tokens))
    elif node.isidentifier():
        return VariableNode(node)
    elif node.isdigit():
        return LiteralNode(int(node))
    else:
        raise ValueError(node, "is an invalid expression")



##############################################################################
# infix
##############################################################################

def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, MathNode):
        return "(" + infix(node.left) + " " + node.op + " " + infix(node.right) + ")"
    elif isinstance(node, VariableNode):
        return node.name
    elif node is None:
        return
    else:
        pass

##############################################################################
# evaluate
##############################################################################


def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if isinstance(node, VariableNode):
        if node.name not in symTbl:
            raise ValueError(node.name, "is invalid")
        else:
            return int(symTbl[node.name])
    elif isinstance(node, LiteralNode):
        return node.val
    elif isinstance(node, MathNode):
        if node.op == "//":
            return evaluate(node.left, symTbl) // evaluate(node.right, symTbl)
        elif node.op == "*":
            return evaluate(node.left, symTbl) * evaluate(node.right, symTbl)
        elif node.op == "+":
            return evaluate(node.left, symTbl) + evaluate(node.right, symTbl)
        else:
            return evaluate(node.left, symTbl) - evaluate(node.right, symTbl)

##############################################################################
# main
##############################################################################


def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""

    print("Hello Herp, welcome to Derp v1.0 :)")

    inFile = input("Herp, enter symbol table file: ")
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    table = {}
    file = open(inFile)
    line=file.readline()

    while line:
        n, v = line.split()
        table[n] = int(v)
        line = file.readline()
    file.close()
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break

        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        token = prefixExp.split(" ")

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF
        # THE PARSE TREE.
        TreeRoot = parse(token)

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        string = infix(TreeRoot)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the infix expression:", string)

        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        evaluation = evaluate(TreeRoot, table)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", evaluation)

    print("Goodbye Herp :(")

if __name__ == "__main__":
    main()
