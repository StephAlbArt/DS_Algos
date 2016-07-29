class _LinkNode:
    def __init__(self, value):
        """
        Create a node element.

        Parameters
        ----------
        value : int, float
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add_to_tail(self, value):
        """
        Add a new node to the tail of the linked list.

        Parameters
        ----------
        value : int, float, string, dict, list, etc.

        """
        new_node = _LinkNode(value)

        if self._head is None:  # if linked list is empty
            self._head = new_node

        if self._tail:  # if linked list has a tail, i.e. > 1 node
            self._tail.next = new_node

        self._tail = new_node  # regardless of current length, update tail

        self._length += 1

    def contains(self, target):
        """
        Determine if a specified value exists in the linked list

        Parameters
        ----------
        target : int, float, string, dict, list, etc.

        Returns
        -------
        bool

        """
        curr_node = self._head

        while curr_node:
            if curr_node.value == target:
                return True
            curr_node = curr_node.next

        return False

    def delete(self, target):
        """
        Delete a node from the linked list if it exists.

        Parameters
        ----------
        target : int, float, string, dict, list, etc.

        Returns
        -------
        Node or None
            If target node found (and deleted) return Node, else return None.

        """
        curr_node = self._head

        if curr_node.value == target:
            found = curr_node
            self._head = curr_node.next
            return found

        while curr_node.next:  # terminates if at end of list
            # we want to look at the next node because in the event that we
            # find a match, we can change the `next` reference of the
            # current node
            if curr_node.next.value == target:
                found = curr_node.next
                curr_node.next = curr_node.next.next
                return found
            curr_node = curr_node.next

        return None

    # STOPPED: need to test this before doing has_cycle