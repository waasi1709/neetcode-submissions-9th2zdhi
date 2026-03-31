#Firstly we want a doubly linked list 
class Node:
    def __init__(self,key,val):
        #I'll be storing key,val pairs in a singular node 
        self.key = key
        self.val = val 
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        #lets setup our doubly linked list and hashmap
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0) 
        self.right = Node(0,0)

        #set the pointers
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        #here node corresponds to the middle position
        #store left and right nodes first
        prev = node.prev
        nxt = node.next
        #now assign left and right nodes to each other
        node.prev.next = nxt
        node.next.prev = prev

    def insert(self,node):
        #we want to always insert at the right most position becasue that corresponds to most-recently used
        #store the right most element and the element before it
        prev , nxt = self.right.prev,self.right
        #insert node after (right-1) element
        #change address of prev.next to new node
        prev.next = nxt.prev = node
        #now point this new node to rightmost thing
        node.next , node.prev = nxt, prev


    def get(self, key: int) -> int:
        #check if key in cache 
        if key in self.cache:
            self.remove(self.cache[key])

            self.insert(self.cache[key])
            return self.cache[key].val 

        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
        
