"""
Given two sorted linked lists,
merge them so that the resulting linked list is also sorted.
Consider two sorted linked lists and the merged list below them as an example.
"""


def merge_sorted(head1, head2):
    if not head1: return head2
    if not head2: return head1

    # 첫 스타트 찾음
    if head1.data <= head2.data:
        new_head = head1
        head1 = head1.next
    else:
        new_head = head2
        head2 = head2.next

    new_tail = new_head
    while head1 and head2:
        temp = None
        if head1.data < head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        new_tail.next = temp
        new_tail = temp

    if head1:
        new_tail.next = head1
    elif head2:
        new_tail.next = head2

    return new_head


print(merge_sorted([4, 8, 15, 19, 22],[7, 9, 10,16]))