class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        next_val = self.next.val if self.next else None
        return f'ListNode({self.val}, next = {next_val})'

def create_linked_list(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for el in values[1:]:
        current.next = ListNode(el)
        current = current.next
    return head

node = ListNode(1)
next_node = ListNode(2)
node.next = next_node
print(node.val)
print(node.next)
print(next_node.val)
print(next_node.next)
print(node.__repr__())
print(create_linked_list([1, 2, 3]))