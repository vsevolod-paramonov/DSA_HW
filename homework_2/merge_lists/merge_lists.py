class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists_with_dummy(list1: ListNode, list2: ListNode):

    dummy = tail = ListNode()

    while list1 and list2:

        ### Если значение в list1 меньше то добавляем указатель на list1 в tail
        if list1.val < list2.val:
            tail.next = list1

            ### Сдвигаем указатель list1
            list1 = list1.next

        ### Иначе делаем это с list2
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    ### Если в одном из list'ов закончились элементы, то добавляем указатель
    ### на оставшиеся элементы из другого list'а
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next



def merge_lists_without_dummy(list1: ListNode, list2: ListNode):

    ### Здесь имеет смысл добавить проверки на пустые списки, потому что
    ### до "while list1 and list2" работаем со значениями, которых может и не быть в узлах
    if not list1:
        return list2
    if not list2:
        return list1


    if list1.val < list2.val:
        head = tail = list1
        list1 = list1.next
    else:
        head = tail = list2
        list2 = list2.next


    while list1 and list2:

        ### Если значение в list1 меньше то добавляем указатель на list1 в tail
        if list1.val < list2.val:
            tail.next = list1

            ### Сдвигаем указатель list1
            list1 = list1.next

        ### Иначе делаем это с list2
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    ### Если в одном из list'ов закончились элементы, то добавляем указатель
    ### на оставшиеся элементы из другого list'а
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return head