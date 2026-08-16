class Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity= capacity
        self.left, self.right= Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        #remove the node
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        #insert the node at the most recently used - right most
        prev_node_from_right = self.right.prev

        node.next = self.right
        node.prev = prev_node_from_right

        prev_node_from_right.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:

            #since the key is used, move it to right before the right most
            #and remove from the current position.
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #key is present update the value and also move it recently used side
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            #if capacity is reached, then remove the left most-least used node
            #and remove it form the cache
            if len(self.cache) >= self.capacity:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
            
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
            