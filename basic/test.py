from basic.linked_list import linked_list

linked = linked_list()

print(linked.to_string())
linked.add(1)
linked.add(8)
linked.add(6)
linked.add(3)
linked.add(2)

print(linked.to_string())
linked.remove(6)
linked.remove(1)
print(linked.to_string())