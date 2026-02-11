class node:
    def __init__(self, new_data = None):
        self.data = new_data
        self.prev = None
        self.next = None

class doubly_circular_linked_list:
    def __init__(self):
        self.head_node = node()
        self.head_node.prev = self.head_node
        self.head_node.next = self.head_node

    @staticmethod
    def generic_insert(start_node, mid_node, end_node):
        mid_node.next = end_node
        mid_node.prev = start_node
        start_node.next = mid_node
        end_node.prev = mid_node

    def insert_end(self, new_data):
        self.generic_insert(self.head_node.prev, node(new_data), self.head_node)

    def show(self):
        print('[START]<->', end='')
        run = self.head_node.next
        while run is not self.head_node:
            print('[', run.data, ']<->', end='')
            run = run.next
        print('[END]')

L = doubly_circular_linked_list()
for i in range(4):
    L.insert_end((i+1) * 5)
L.show()
#-----------------------------------------------
# Count 2
class node:
    def __init__(self, new_data = None):
        self.data = new_data
        self.prev = None
        self.next = None

class doubly_circular_linked_list:
    def __init__(self):
        self.head_node = node()
        self.head_node.prev = self.head_node
        self.head_node.next = self.head_node

    @staticmethod
    def generic_insert(start_node, mid_node, end_node):
        mid_node.next = end_node
        mid_node.prev = start_node
        start_node.next = mid_node
        end_node.prev = mid_node

    def insert_end(self, new_data):
        self.generic_insert(self.head_node.prev, node(new_data), self.head_node)

    def show(self):
        print('[START]<->', end='')
        run = self.head_node.next
        while run is not self.head_node:
            print('[', run.data, ']<->', end='')
            run = run.next
        print('[END]')

L = doubly_circular_linked_list()
for i in range(4):
    L.insert_end(i*5)
L.show()

















