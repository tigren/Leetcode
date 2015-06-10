# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def listnode_to_num(list_node):

    num, digit = 0, 0
    
    while list_node is not None:           
        num += list_node.val * 10 ** digit          
        digit += 1
        list_node = list_node.next
    return num
    
def num_to_listnode(num):
    
    # solution from Stackoverflow, 342 -> [3,4,2]
    list_of_ints = [int(i) for i in str(num)]
    list_of_ints.reverse()
    previous_node, first_node = None, None
    
    for digit in list_of_ints:
        node = ListNode(digit)
        if first_node is None:
            first_node = node
        if previous_node is not None:
            previous_node.next = node
            previous_node = node
        else:
            # same condition with first node
            previous_node = previous_node

    return first_node

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        
        sum = listnode_to_num(l1) + listnode_to_num(l2)
		
        return num_to_listnode(sum)