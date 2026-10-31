class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head: ListNode | None = None) -> ListNode | None:
    new_list = None
    while head:
        next_node = head.next
        head.next = new_list
        new_list = head
        head = next_node
    return new_list
