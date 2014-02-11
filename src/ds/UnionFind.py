'''
Created on Feb 10, 2014

@author: anuvrat
'''

class QuickFind(object):
    def __init__(self, size, debug = False):
        self.group_count = self.size = size
        self.group = [i for i in range(size)]
        self.debug = debug
        
    def union(self, child, parent):
        ''' Complexity = O(n) '''
        if self.group[child] == self.group[parent]: return
        
        self.group = [self.group[parent] if self.group[idx] == self.group[child] else self.group[idx] for idx in range(self.size)]
        self.group_count = self.group_count - 1
        if self.debug: print(self.group_count, self.group)
        
    def find(self, element):
        ''' Complexity = O(1) '''
        return self.group[element]
    
    def get_count_of_groups(self):
        return self.group_count
    
    def connected(self, element_a, element_b):
        ''' Complexity = O(1) '''
        return self.group[element_a] == self.group[element_b]
    
class WeightedQuickUnion(object):
    def __init__(self, size, debug = False):
        self.group_count = self.size= size
        self.group = [i for i in range(size)]
        self.tree_size = [1] * size
        self.debug = debug
    
    def union(self, child, parent):
        ''' Complexity = O(lg n) '''
        child_root = self.find(child)
        parent_root = self.find(parent) 
        
        if child_root == parent_root : return
        
        # push the smaller tree into the larger tree to reduce tree height
        new_tree_size = self.tree_size[parent_root] + self.tree_size[child_root]
        if self.tree_size[child_root] < self.tree_size[parent_root] : 
            self.group[child_root] = self.group[parent_root]
            self.tree_size[parent_root] = new_tree_size
        else: 
            self.group[parent_root] = self.group[child_root]
            self.tree_size[child_root] = new_tree_size
        self.group_count = self.group_count - 1
        if self.debug: print(self.group_count, self.group, self.tree_size)
        
    
    def find(self, element):
        ''' Complexity = O(lg n) '''
        while self.group[element] != element:
            self.group[element] = self.group[self.group[element]]   # Compress the path by bringing up the subtree by 1 level
            element = self.group[element]
        return element
    
    def get_count_of_groups(self):
        return self.group_count
    
    def connected(self, element_a, element_b):
        ''' Complexity = O(lg n) '''
        return self.find(element_a) == self.find(element_b)

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
    
    qu = WeightedQuickUnion(10, True)
    qu.union(4, 3)
    qu.union(3, 8)
    qu.union(6, 5)
    qu.union(9, 4)
    qu.union(2, 1)
    qu.union(5, 0)
    qu.union(7, 2)
    qu.union(6, 1)
    qu.union(7, 3)