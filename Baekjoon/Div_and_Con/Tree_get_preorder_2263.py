def print_pre_order(in_ofs_s, in_ofs_e, post_ofs_s, post_ofs_e, inorder, postorder): 
    if in_ofs_e < in_ofs_s : return None
    elif in_ofs_s == in_ofs_e: 
        print(inorder[in_ofs_s], end=' ')
    else: 
        root = postorder[post_ofs_e]
        post_ofs_e -= 1
        print(root, end=' ')
        root_idx = 0
        while inorder[in_ofs_s+root_idx] != root: 
            root_idx += 1
        print_pre_order(in_ofs_s, in_ofs_s+root_idx-1, post_ofs_s, post_ofs_s+root_idx-1, inorder, postorder)
        print_pre_order(in_ofs_s+root_idx+1, in_ofs_e, post_ofs_s+root_idx, post_ofs_e, inorder, postorder)

import sys
sys.stdin = open('Algorithm/Baekjoon/Div_and_Con/Tree_get_preorder_2263_test_input.txt', 'r')
sys.setrecursionlimit(10000)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
print_pre_order(0, N-1, 0, N-1, inorder, postorder)