class Node:
    def __init__(self, children = []):
        self.parent, self.children = None, []
        
        for node in children:
            self.add(node)

    def add(self, node):
        node.parent = self
        self.children.append(node)

    def cut(self):
        if self.parent != None:
            self.parent.children.remove(self)
        
        self.parent = None

    def flood(self, function):
        function(self)
        for node in self.children:
            node.flood(function)
    
class Navigator:
    def __init__(self, current_node):
        self.current_node = current_node

    def navigate_up(self):
        if self.current_node.parent is None:
            raise TopOfTreeException()
        else:
            self.current_node = self.current_node.parent
    
    def navigate_down(self, index = 0):
        if len(self.current_node.children) == 0:
            raise BottomOfTreeException()
        else:
            self.current_node = self.current_node.children[index]

class DeadEndException(Exception):
    def __init__(self, message = "A dead end has been reached"):
        super().__init__(message)

class TopOfTreeException(DeadEndException):
    def __init__(self, message = "The top of the tree has been reached"):
        super().__init__(message)

class BottomOfTreeException(DeadEndException):
    def __init__(self, message = "The bottom of the tree has been reached"):
        super().__init__(message)
