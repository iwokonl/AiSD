from typing import Any

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,val: Any):
        self.value=val
        self.left_child=None
        self.right_child=None

    def min(self):
        if self.left_child!=None:
            return self.left_child.min()
        return self

    def _contains(self, value: Any):
        #print(f'{self.value}?{value}')
        if self.value == value:
            return True
        elif self.value > value:
            if self.left_child!=None:
                return self.left_child._contains(value)
            else:
                return False
        else:
            if self.right_child!=None:
                return self.right_child._contains(value)
            else:
                return False

    def show(self,level):
        if self.right_child!=None:
                self.right_child.show(level+1)
        print(' ' * 4 * level + '->', self.value)
        if self.left_child!=None:
            self.left_child.show(level+1)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, node: 'BianryNode'):
        self.root=node

    def insert(self, value: Any):
        self.root= self._insert(self.root,value)

    def _insert(self, node: BinaryNode, value: Any):
        if value<node.value:
            if node.left_child==None:
                node.left_child=BinaryNode(value)
            else:
                self._insert(node.left_child,value)
        else:
            if node.right_child==None:
                node.right_child=BinaryNode(value)
            else:
                self._insert(node.right_child,value)
        return node
    
    def insertlist(self, lista):
        for element in lista:
            self.insert(element)

    def contains(self, value: Any):
        return self.root._contains(value)

    def remove(self, value: Any):
        self.root= self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any):
        if node!=None:
            if value == node.value:
                if((node.left_child==None)&(node.right_child==None)):
                    return None
                elif node.left_child==None:
                    return node.right_child
                elif node.right_child==None:
                    return node.left_child
                node.value=node.right_child.min().value
                node.right_child=self._remove(node.right_child,node.value)
            elif value < node.value:
                node.left_child=self._remove(node.left_child,value)
            else:
                node.right_child=self._remove(node.right_child,value)
        return node

    def show(self):
       self.root.show(0)