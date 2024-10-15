class Node:
    def __init__(self, label):
        self.label = label
        # Todo nó tem no máximo 2 filhos
        # Esquerda é menor
        # Direita é maior
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        # Cria um novo nó
        node = Node(label)

        # Verifico se a árvore está vazia
        if self.empty():
            self.root = node
        else:
            # Árvore não vazia
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:
                    dad_node = curr_node

                    # Verifica se vai para esquerda ou direita
                    if node.getLabel() < curr_node.getLabel():
                        # Vai para esquerda
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    # Se curr_node é None, então encontrou onde inserir
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    break  # Sair do loop ao inserir o nó

    def empty(self):
        return self.root is None

    def show(self, curr_node):
        if curr_node is not None:  # Adicionando verificação para parar a recursão
            print('%d' % curr_node.getLabel(), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

    def remove(self, label):
        '''
        3 Casos:
        1. Nó a ser removido não tem filhos
        2. Nó a ser removido tem somente um filho
        3. Nó a ser removido tem dois filhos
        '''
        dad_node = None
        curr_node = self.root

        while curr_node is not None:
            # Verifica se encontrou o nó a ser removido
            if label == curr_node.getLabel():
                # Caso 1: Nó Folha
                if curr_node.getLeft() is None and curr_node.getRight() is None:
                    # Verifico se é a raiz
                    if dad_node is None:
                        self.root = None
                    else:
                        # Verifica se é filho à esquerda ou direita
                        if dad_node.getLeft() == curr_node:
                            dad_node.setLeft(None)
                        elif dad_node.getRight() == curr_node:
                            dad_node.setRight(None)
                # Caso 2: Somente um filho
                elif (curr_node.getLeft() is None and curr_node.getRight() is not None) or (curr_node.getLeft() is not None and curr_node.getRight() is None):
                    # Verifico se é a raiz
                    if dad_node is None:
                        if curr_node.getLeft() is not None:
                            self.root = curr_node.getLeft()
                        else:
                            self.root = curr_node.getRight()
                    else:
                        if curr_node.getLeft() is not None:
                            if dad_node.getLeft() == curr_node:
                                dad_node.setLeft(curr_node.getLeft())
                            else:
                                dad_node.setRight(curr_node.getLeft())
                        else:
                            if dad_node.getLeft() == curr_node:
                                dad_node.setLeft(curr_node.getRight())
                            else:
                                dad_node.setRight(curr_node.getRight())
                # Caso 3: o nó a ser removido possui dois filhos
                elif curr_node.getLeft() is not None and curr_node.getRight() is not None:
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    next_smaller = smaller_node.getLeft()

                    while next_smaller is not None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.getLeft()

                    # Verifica se o nó a ser removido é a raiz
                    if dad_node is None:
                        self.root = smaller_node
                    else:
                        if dad_node.getLeft() == curr_node:
                            dad_node.setLeft(smaller_node)
                        else:
                            dad_node.setRight(smaller_node)

                    # Verifica se o smaller_node tem um filho à direita (não pode ter filho à esquerda)
                    if dad_smaller_node != curr_node:
                        dad_smaller_node.setLeft(smaller_node.getRight())
                        smaller_node.setRight(curr_node.getRight())

                    smaller_node.setLeft(curr_node.getLeft())

                break

            dad_node = curr_node
            # Verifica se vai para esquerda ou direita
            if label < curr_node.getLabel():
                curr_node = curr_node.getLeft()
            else:
                curr_node = curr_node.getRight()


# Testando a árvore
t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.remove(6)

# Mostrar a árvore em pré-ordem
t.show(t.getRoot())
