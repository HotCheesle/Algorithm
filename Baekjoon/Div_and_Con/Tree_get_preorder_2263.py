def make_tree(p_in, parent, is_right): 
    if not p_in : return None
    elif len(p_in) == 1: 
        if is_right: 
            nodes[parent][2] = p_in[0]
            confirmed.add(p_in[0])
        else: 
            nodes[parent][1] = p_in[0]
            confirmed.add(p_in[0])
    else: 
        root = postorder.pop()
        while root in confirmed: 
            root = postorder.pop()
        confirmed.add(root)
        if is_right: 
            nodes[parent][2] = root
        else: 
            nodes[parent][1] = root
        root_idx = p_in.index(root)
        make_tree(p_in[root_idx+1:], root, True)
        make_tree(p_in[:root_idx], root, False)

def pre_order(root): 
    if root == -1: return None
    print(root, end=' ')
    pre_order(nodes[root][1])
    pre_order(nodes[root][2])

import sys
sys.stdin = open('Algorithm/Baekjoon/Div_and_Con/Tree_get_preorder_2263_test_input.txt', 'r')

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
confirmed = set()
nodes = list([i, -1, -1] for i in range(N+1)) # (node, left, right)
root = postorder[-1]
make_tree(inorder, 0, True) # root의 부모는 0(없음)
pre_order(root)