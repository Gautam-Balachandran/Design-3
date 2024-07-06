# Time Complexity : O(1)
# Space Complexity : O(n), where n is the capacity of the cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: Node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self) -> Node:
        res = self.tail.prev
        self.remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if not node:
            new_node = Node(key, value)
            self.map[key] = new_node
            self.add_to_head(new_node)
            if len(self.map) > self.capacity:
                tail = self.remove_tail()
                del self.map[tail.key]
        else:
            node.value = value
            self.move_to_head(node)

# Examples

# Example 1

cache = LRUCache(2)
cache.put(1, 1)             # Cache is {1=1}
cache.put(2, 2)             # Cache is {1=1, 2=2}
print(cache.get(1))         # Returns 1, Cache is {2=2, 1=1}
cache.put(3, 3)             # Evicts key 2, Cache is {1=1, 3=3}
print(cache.get(2))         # Returns -1 (not found)
cache.put(4, 4)             # Evicts key 1, Cache is {4=4, 3=3}
print(cache.get(1))         # Returns -1 (not found)
print(cache.get(3))         # Returns 3, Cache is {4=4, 3=3}
print(cache.get(4))         # Returns 4, Cache is {3=3, 4=4}

# Example 2

cache = LRUCache(1)
cache.put(2, 1)             # Cache is {2=1}
print(cache.get(2))         # Returns 1, Cache is {2=1}
cache.put(3, 2)             # Evicts key 2, Cache is {3=2}
print(cache.get(2))         # Returns -1 (not found)
print(cache.get(3))         # Returns 2, Cache is {3=2}

# Example 3

cache = LRUCache(3)
cache.put(1, 1)             # Cache is {1=1}
cache.put(2, 2)             # Cache is {1=1, 2=2}
cache.put(3, 3)             # Cache is {1=1, 2=2, 3=3}
print(cache.get(1))         # Returns 1, Cache is {2=2, 3=3, 1=1}
cache.put(4, 4)             # Evicts key 2, Cache is {3=3, 1=1, 4=4}
print(cache.get(2))         # Returns -1 (not found)
print(cache.get(3))         # Returns 3, Cache is {1=1, 4=4, 3=3}
print(cache.get(4))         # Returns 4, Cache is {1=1, 3=3, 4=4}