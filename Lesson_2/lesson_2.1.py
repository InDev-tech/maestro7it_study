class ListNode:
    """
    Узел односвязного списка (Linked List Node).
    
    Это фундаментальная структура данных, представляющая один элемент связного списка.
    Каждый узел содержит данные (значение) и ссылку на следующий узел в последовательности.
    
    Атрибуты:
        val (Any): Значение, хранящееся в узле. Может быть любого типа данных.
        next (ListNode, optional): Ссылка на следующий узел в списке. 
                                  Если узел последний, next = None.
    
    Примеры:
        >>> node = ListNode(5)
        >>> node.val
        5
        >>> node.next
        None
        
        >>> node1 = ListNode(1)
        >>> node2 = ListNode(2)
        >>> node1.next = node2
        >>> node1.next.val
        2
    """
    
    def __init__(self, val=0, next=None):
        """
        Инициализирует новый узел связного списка.
        
        Args:
            val (Any, optional): Значение для хранения в узле. По умолчанию 0.
            next (ListNode, optional): Ссылка на следующий узел. По умолчанию None.
        
        Returns:
            None
            
        Временная сложность: O(1)
        Пространственная сложность: O(1)
            
        Примеры:
            >>> node = ListNode()           # Создает узел со значением 0
            >>> node = ListNode(42)         # Создает узел со значением 42
            >>> node = ListNode("hello")    # Создает узел со строковым значением
            >>> next_node = ListNode(2)
            >>> node = ListNode(1, next_node)  # Создает узел со значением 1, ссылающийся на next_node
        """
        self.val = val      # Значение узла
        self.next = next    # Ссылка на следующий узел
    
    def __repr__(self):
        """
        Возвращает строковое представление узла для отладки.
        
        Метод используется при вызове repr() или при выводе в консоли.
        Показывает значение текущего узла и значение следующего узла (если он существует).
        
        Returns:
            str: Строковое представление узла в формате "ListNode(val, next=next_val)"
            
        Примеры:
            >>> node = ListNode(5)
            >>> repr(node)
            'ListNode(5, next=None)'
            
            >>> node1 = ListNode(1)
            >>> node2 = ListNode(2)
            >>> node1.next = node2
            >>> repr(node1)
            'ListNode(1, next=2)'
            
            >>> repr(node2)
            'ListNode(2, next=None)'
        """
        next_val = self.next.val if self.next else None
        return f"ListNode({self.val}, next={next_val})"
    
    def __str__(self):
        """
        Возвращает упрощенное строковое представление узла.
        
        Returns:
            str: Строковое представление значения узла
            
        Пример:
            >>> node = ListNode(10)
            >>> str(node)
            '10'
        """
        return str(self.val)


def create_linked_list(values: list) -> ListNode:
    """
    Создает связный список из списка значений.
    
    Args:
        values (list): Список значений для преобразования в связный список.
                      Может быть пустым.
    
    Returns:
        ListNode: Голова (первый узел) созданного связного списка.
                 Возвращает None, если список values пуст.
    
    Raises:
        TypeError: Если values не является списком или итерируемым объектом.
    
    Временная сложность: O(n), где n - количество элементов в values
    Пространственная сложность: O(n)
    
    Примеры:
        >>> head = create_linked_list([1, 2, 3, 4, 5])
        >>> # Создает список: 1 → 2 → 3 → 4 → 5 → None
        
        >>> head = create_linked_list([])
        >>> head is None
        True
        
        >>> head = create_linked_list(["a", "b", "c"])
        >>> # Создает список: "a" → "b" → "c" → None
    """
    if not values:
        return None
    
    # Создаем голову списка
    head = ListNode(values[0])
    current = head
    
    # Добавляем остальные элементы
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head


def print_linked_list(head: ListNode, separator: str = " → ", end_marker: str = " → None") -> None:
    """
    Печатает значения связного списка в читаемом формате.
    
    Args:
        head (ListNode): Голова связного списка для печати.
        separator (str, optional): Разделитель между значениями узлов. По умолчанию " → ".
        end_marker (str, optional): Маркер конца списка. По умолчанию " → None".
    
    Returns:
        None
    
    Временная сложность: O(n), где n - количество узлов в списке
    Пространственная сложность: O(n) для временного хранения строки
    
    Примеры:
        >>> head = create_linked_list([1, 2, 3])
        >>> print_linked_list(head)
        1 → 2 → 3 → None
        
        >>> print_linked_list(head, separator=" -> ", end_marker=" -> END")
        1 -> 2 -> 3 -> END
        
        >>> print_linked_list(None)
        None
    """
    if head is None:
        print("None")
        return
    
    current = head
    values = []
    
    while current:
        values.append(str(current.val))
        current = current.next
    
    print(separator.join(values) + end_marker)


def linked_list_to_list(head: ListNode) -> list:
    """
    Преобразует связный список в обычный Python список.
    
    Args:
        head (ListNode): Голова связного списка для преобразования.
    
    Returns:
        list: Список значений из связного списка в порядке их следования.
              Возвращает пустой список, если head = None.
    
    Временная сложность: O(n), где n - количество узлов
    Пространственная сложность: O(n) для результирующего списка
    
    Примеры:
        >>> head = create_linked_list([1, 2, 3])
        >>> linked_list_to_list(head)
        [1, 2, 3]
        
        >>> linked_list_to_list(None)
        []
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def get_linked_list_length(head: ListNode) -> int:
    """
    Вычисляет длину (количество узлов) связного списка.
    
    Args:
        head (ListNode): Голова связного списка.
    
    Returns:
        int: Количество узлов в связном списке.
             Возвращает 0, если список пуст (head = None).
    
    Временная сложность: O(n), где n - количество узлов
    Пространственная сложность: O(1)
    
    Примеры:
        >>> head = create_linked_list([1, 2, 3])
        >>> get_linked_list_length(head)
        3
        
        >>> get_linked_list_length(None)
        0
    """
    length = 0
    current = head
    
    while current:
        length += 1
        current = current.next
    
    return length


# Демонстрация использования
if __name__ == "__main__":
    # Пример 1: Создание списка вручную
    print("=" * 50)
    print("Пример 1: Создание списка вручную")
    print("=" * 50)
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    
    node1.next = node2
    node2.next = node3
    
    print(f"node1: {node1}")
    print(f"node1.next: {node1.next}")
    print(f"node2.next: {node2.next}")
    print(f"Полный список: ", end="")
    print_linked_list(node1)
    
    # Пример 2: Использование вспомогательных функций
    print("\n" + "=" * 50)
    print("Пример 2: Использование вспомогательных функций")
    print("=" * 50)
    
    head = create_linked_list([10, 20, 30, 40, 50])
    print("Создан список:")
    print_linked_list(head)
    
    print(f"\nДлина списка: {get_linked_list_length(head)}")
    print(f"Список как Python list: {linked_list_to_list(head)}")
    
    # Пример 3: Работа с пустым списком
    print("\n" + "=" * 50)
    print("Пример 3: Работа с пустым списком")
    print("=" * 50)
    
    empty_head = create_linked_list([])
    print(f"Пустой список: ", end="")
    print_linked_list(empty_head)
    print(f"Длина пустого списка: {get_linked_list_length(empty_head)}")
    print(f"Пустой список как Python list: {linked_list_to_list(empty_head)}")
    
    # Пример 4: Список с разными типами данных
    print("\n" + "=" * 50)
    print("Пример 4: Список с разными типами данных")
    print("=" * 50)
    
    mixed_head = create_linked_list(["Python", 3.14, True, [1, 2, 3], {"key": "value"}])
    print("Смешанный список:")
    print_linked_list(mixed_head)
    
    # Пример 5: Проверка документации
    print("\n" + "=" * 50)
    print("Пример 5: Документация класса ListNode")
    print("=" * 50)
    
    print(ListNode.__doc__)