# Last updated: 1/22/2026, 12:13:01 PM
class Node(object):
    def __init__(self, data, key):
        self.data = data
        self.next = None
        self.prev = None
        self.key = key
        # update lru by removing and then adding
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity < 0:
            capacity = -1 * capacity 
        self.capacity = capacity
        self.head = None # insert here
        self.tail = None # lru here
        self.cache = {} # {key:Node} -> O(1) search


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # search algo
        if key in self.cache:
            # move this to front
            self.list_remove(self.cache[key])
            self.list_insert(self.cache[key])

            return self.cache[key].data
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if get(key) == -1:
        #   if len() > cap:
        #       pop lru_key 
        #       {key:value}
        if self.get(key) != -1: # existing key, change lru
            self.cache[key].data = value
        else:
            self.cache[key] = Node(value, key)
            self.list_insert(self.cache[key])
            if len(self.cache) > self.capacity: # add as head
                lru = self.tail # remove will replace self.tail
                self.list_remove(lru)
                del self.cache[lru.key]


    def list_remove(self, node):
        if node.prev != None:
            node.prev.next = node.next # disconect
        else:
            self.head = node.next

        if node.next != None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def list_insert(self, node):        
        # add to front 
        node.next = self.head 
        if self.head != None:
            self.head.prev = node
        else: # empty list
            self.tail = node

        self.head = node
        node.prev = None
        


        

# head is lru
# when new item is assi

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)