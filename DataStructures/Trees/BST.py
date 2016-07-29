class _TreeNode:
    def __init__(self, key, value=None):
        """
        Create a node element.

        Parameters
        ----------
        key : int, float
        value : any type, optional
        """
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self._root = None

    def contains(self, key_to_find, node='__ignored__'):
        """
        Recursively determine if a specified value exists in the tree.

        Parameters
        ----------
        key_to_find : int, float
        node : _Node, optional
            Default value is 'ignored'; serves simply as a flag.

        Returns
        -------
        bool

        """
        # set default value if node parameter not specified
        if node is '__ignored__':
            node = self._root

        # if node is still None (empty tree)
        if node is None:
            return False
        elif node.key == key_to_find:
            return True
        elif key_to_find < node.key:  # visit left child
            return self.contains(key_to_find, node.left)
        else:  # visit right child
            return self.contains(key_to_find, node.right)
