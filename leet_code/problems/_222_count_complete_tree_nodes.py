def countNodes_O_of_N(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0

    left = self.countNodes(root.left)
    right = self.countNodes(root.right)

    return 1 + left + right


def MycountNodes(self, root):

    def find_full_levels_height(root):
        if not root:
            return 0

        left = find_full_levels_height(root.left)

        return 1 + left

    height = find_full_levels_height(root)

    def exists_at_position(position):

        if root and not root.left and not root.right:
            return 1

        binary = bin(position)[2:].zfill(height)

        current = root

        for char in binary:
            if char == "0":
                current = current.left
            else:
                current = current.right
            if not current:
                return False
        return True

    if not root:
        return 0

    full_levels_nodes = 2 ** (height) - 1

    lower_bound = 0
    upper_bound = full_levels_nodes

    last_level_nodes = 0
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if exists_at_position(mid):
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1

    return 1 + full_levels_nodes + upper_bound


def countNodes_claude_ai(self, root):
    if not root:
        return 0

    # Calcola l'altezza dell'albero
    def get_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    height = get_height(root)

    # Se l'albero è completamente pieno
    if height == 0:
        return 0

    # Verifica l'esistenza del nodo in una posizione specifica
    def node_exists(position):
        node = root
        for bit in bin(position)[2:].zfill(height - 1):
            node = node.left if bit == "0" else node.right
            if not node:
                return False
        return True

    # Ricerca binaria sull'ultimo livello
    left, right = 0, 2 ** (height - 1) - 1
    while left <= right:
        mid = (left + right) // 2
        if node_exists(mid):
            left = mid + 1
        else:
            right = mid - 1

    # Calcola il numero totale di nodi
    return (1 << height) - 1 + left
