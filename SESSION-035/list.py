print('9th Oct 2025')

class Node: 
    def __init__(self, new_data): 
        self.data = new_data 
        self.prev = None 
        self.next = None 


class List: 
    def __init__(self): 
        self.head_node = Node(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node

    @staticmethod 
    def generic_insert(start, mid, end): 
        mid.next = end 
        mid.prev = start 
        start.next = mid 
        end.prev = mid 

    @staticmethod 
    def generic_delete(N): 
        N.prev.next = N.next 
        N.next.prev = N.prev 

    def insert_start(self, new_data): 
        self.generic_insert(self.head_node, Node(new_data), self.head_node.next)

    def insert_end(self, new_data): 
        self.generic_insert(self.head_node.prev, Node(new_data), self.head_node) 

    def show(self): 
        run = self.head_node.next 
        print('[START]<->', end='')
        while run is not self.head_node: 
            print('[', run.data, ']<->', end='')
            run = run.next 
        print('[END]')


if __name__ == '__main__': 
    lst = List() 
    for x in range(5): 
        lst.insert_end((x+1) * 10)
    lst.show()

