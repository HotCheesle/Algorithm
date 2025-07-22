import sys

class Node: 
    def __init__(self, num): 
        self.num = num
        self.pre = None
        self.next = None
        
    def print_stdu_num(self): 
        print(self.num, end=" ")
    
def insert_num(head, tail, stu_num, num): 
    new_node = Node(stu_num)
    if num == 0: 
        tail.next = new_node
        new_node.pre = tail
        tail = new_node
        return head, tail
    c_node = tail
    for i in range(num - 1): 
        c_node = c_node.pre
    if c_node is head: 
        new_node.next = head
        head.pre = new_node
        head = new_node
        return head, tail
    (c_node.pre).next = new_node
    new_node.pre = c_node.pre
    c_node.pre = new_node
    new_node.next = c_node
    return head, tail

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

head = None
tail = None
for i in range(n): 
    if head is None: 
        head = Node(i)
        tail = head
    else: 
        insert_num(head, tail, i, nums[i])

node = head
while node.next is not None: 
     node.print_stdu_num()
     