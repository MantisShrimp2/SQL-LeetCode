# Last updated: 3/6/2026, 11:58:07 AM
1class LRUCache(object):
2
3    def __init__(self, capacity):
4        """
5        :type capacity: int
6        """
7        self.capacity = capacity
8        self.values = OrderedDict()
9        
10
11    def get(self, key):
12        """
13        :type key: int
14        :rtype: int
15        """
16        if key not in self.values:
17            return -1
18        else:
19            self.values[key] = self.values.pop(key)
20            return self.values[key]
21
22    def put(self, key, value):
23        """
24        :type key: int
25        :type value: int
26        :rtype: None
27        """
28        if key not in self.values:
29            if len(self.values) == self.capacity:
30                self.values.popitem(last=False)
31        else:
32                self.values.pop(key)
33        self.values[key] = value
34
35        
36
37
38# Your LRUCache object will be instantiated and called as such:
39# obj = LRUCache(capacity)
40# param_1 = obj.get(key)
41# obj.put(key,value)