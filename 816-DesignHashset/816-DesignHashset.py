# Last updated: 2/27/2026, 9:06:23 PM
class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hashidx(self,key):
        idx = key % self.size
        return idx
    def add(self, key):
        """
        :type key: int
        :rtype: None
        
        """
        idx = self.hashidx(key)
        bucket = self.buckets[idx]
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)
            
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hashidx(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx = self.hashidx(key)
        return key in self.buckets[idx]
        
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)