"""
ListNode (узел списка) — это основной строительный элемент связного списка (Linked List) в программировании.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Значение узла
        self.next = next    # Ссылка на следующий узел
    
    def __repr__(self):
        """Удобное строковое представление для отладки"""
        return f"ListNode({self.val}, next={self.next.val if self.next else None})"

# Создаем узлы
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Связываем узлы
node1.next = node2
node2.next = node3

# Теперь имеем список: 1 → 2 → 3

print(node1.next, node2.next)
