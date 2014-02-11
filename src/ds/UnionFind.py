'''
Created on Feb 10, 2014

@author: anuvrat
'''

class QuickFind(object):

    def __init__(self, size, debug = False):
        self.size = size
        self.group = [i for i in range(size)]
        self.group_count = size
        self.debug = debug
        
    def union(self, child, parent):
        if self.group[child] == self.group[parent]: return
        parent_id = self.group[parent]
        child_id = self.group[child]
        for idx in range(self.size):
            if self.group[idx] == child_id: self.group[idx] = parent_id
        self.group_count = self.group_count - 1
        if self.debug: print(self.group_count, self.group)
        
    def find(self, element):
        if element >= self.size: raise Exception("Invalid element")
        return self.group[element]
    
    def get_count_of_groups(self):
        return self.group_count
    
    def connected(self, element_a, element_b):
        if element_a >= self.size or element_b >= self.size: raise Exception("Invalid element")
        return self.group[element_a] == self.group[element_b]
    

if __name__ == '__main__':
    qf = QuickFind(10, True)
    qf.union(4, 3)
    qf.union(3, 8)
    qf.union(6, 5)
    qf.union(9, 4)
    qf.union(2, 1)
    qf.union(8, 9)
    print(qf.connected(5, 0))
    qf.union(5, 0)
    qf.union(7, 2)
    qf.union(6, 1)