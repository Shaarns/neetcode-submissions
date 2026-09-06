class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next, self.prev = None, None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert_node(self, new_node): #insert_node at the right (most used)
        prev_node = self.right.prev

        new_node.next = self.right
        new_node.prev = prev_node

        self.right.prev = new_node
        prev_node.next = new_node
        
    def remove(self, node): #remove the node
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            new_node = Node(key, value)
            self.remove(self.cache[key])
            self.insert_node(new_node)
            self.cache[key] = new_node
            
        else:
            new_node = Node(key, value)
            if len(self.cache) >= self.capacity:
                node = self.left.next
                self.remove(node)
                del self.cache[node.key]

            self.insert_node(new_node)
            self.cache[key] = new_node


        
