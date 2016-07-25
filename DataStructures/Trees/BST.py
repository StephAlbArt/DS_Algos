class _Node:
    def __init__(self, key, value):
        """
        Create a node element

        Keyword arguments:
        key: int, float
        value (optional): any type
        """
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self._root = None

    def contains(self, find_this_key, node='__ignored__'):
        """
        Determine if a specified value exists in the tree

        Parameters
        ----------
        find_this_key: int or float
        node:  _Node, optional
            Default value is 'ignored'; serves simply as a flag

        Returns
        -------
        boolean
            Whether or not specified value exists in tree

        """
        # set default value if node parameter not specified
        if node is '__ignored__':
            node = self._root

        # if node is still None (empty tree)
        if node is None:
            return False
        elif node.key == find_this_key:
            return True
        elif find_this_key < node.key:  # visit left child
            return self.contains(find_this_key, node.left)
        else:  # visit right child
            return self.contains(find_this_key, node.right)