class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize the capacity
        self.capacity = capacity
        self.hashmap = {}
        self.least_recent = Node(0,0)
        self.most_recent = Node(0,0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent
    
    # updating the linkedlist
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.most_recent.prev, self.most_recent
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        # update the recent of the func
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])
        
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:

        # add the key value pair
        if key in self.hashmap: # if the key already exist
            #update the recency of the key val
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            self.hashmap[key].val = value # update the val

        else: # if key not already exist
            self.hashmap[key] = Node(key, value) # create a new node and add it to the hashmap
            self.insert(self.hashmap[key])

            # check if the size hits capacity
            if len(self.hashmap) > self.capacity:
                # get the least recent node
                lru = self.least_recent.next
                # remove the least recent node from linked list
                self.remove(lru)
                # remove the least recent node from hashmap
                del self.hashmap[lru.key]

        # already exist --> add it to the key
        # if key in self.hashmap:
        #     self.hashmap[key] = value
        #     self.queue.append(key)

        # # if not --> add pair
        # else:
        #     # remove the least recent ele pair first
        #     if len(self.hashmap) >= self.capacity:
        #         least_recent_key = self.queue.popleft() 
        #         del self.hashmap[least_recent_key] # delete least recent key val pairs

        #     # add new value pairs
        #     self.hashmap[key] = value
        #     self.queue.append(key)

        # if the new pair causes exceeding capacity, remove least recently used key
        # queue to store the recent element??
        # popleft 
        # hashmap to store the key and value pairs

        # if the size of hashmap becomes the capacity
        #   remove the queue from the left
        #   remove the popped key val pair from the hashmap
