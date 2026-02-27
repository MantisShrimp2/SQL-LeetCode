# Last updated: 2/27/2026, 5:28:13 PM
1class MyHashSet(object):
2
3    def __init__(self):
4        self.size = 1000
5        self.buckets = [[] for _ in range(self.size)]
6    
7    def hashidx(self,key):
8        idx = key % self.size
9        return idx
10    def add(self, key):
11        """
12        :type key: int
13        :rtype: None
14        
15        """
16        idx = self.hashidx(key)
17        bucket = self.buckets[idx]
18        if key not in self.buckets[idx]:
19            self.buckets[idx].append(key)
20            
21        
22
23    def remove(self, key):
24        """
25        :type key: int
26        :rtype: None
27        """
28        idx = self.hashidx(key)
29        if key in self.buckets[idx]:
30            self.buckets[idx].remove(key)
31        
32
33    def contains(self, key):
34        """
35        :type key: int
36        :rtype: bool
37        """
38        idx = self.hashidx(key)
39        return key in self.buckets[idx]
40        
41        
42
43
44# Your MyHashSet object will be instantiated and called as such:
45# obj = MyHashSet()
46# obj.add(key)
47# obj.remove(key)
48# param_3 = obj.contains(key)