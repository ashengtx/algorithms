import sys

sys.path.append('/home/sheng/Code/python/algorithms')

import operator
from basic.stack.stack import Stack
from mybinarytree import BinaryTree

def build_parse_tree(fpexp):
    """
    建立解析树
    """
    fplist = fpexp.split()
    ptree = BinaryTree('')
    tstack = Stack()
    tstack.push(ptree)
    cur_tree = ptree

    for ch in fplist:
        if ch == '(':
            cur_tree.insert_left('')
            tstack.push(cur_tree)
            cur_tree = cur_tree.get_left_child()
        elif ch not in "+-*/)":
            cur_tree.set_root_value(float(ch))
            cur_tree = tstack.pop()
        elif ch in "+-*/":
            cur_tree.set_root_value(ch)
            cur_tree.insert_right('')
            tstack.push(cur_tree)
            cur_tree = cur_tree.get_right_child()
        elif ch == ')':
            cur_tree = tstack.pop()
        else:
            raise ValueError

    return ptree

def evaluate(parse_tree):
    """
    计算表达式解析树的结果
    """
    opers = {'+':operator.add,
             '-':operator.sub,
             '*':operator.mul,
             '/':operator.truediv}

    lchild = parse_tree.get_left_child()
    rchild = parse_tree.get_right_child()
    val = parse_tree.get_root_value()

    if lchild and rchild:
        # 这里其实有个问题，可能存在非法表达式的情况，即左右节点一个为空，另一个不为空
        return opers[val](evaluate(lchild), evaluate(rchild))
    else:
        return val

ptree = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(ptree))
