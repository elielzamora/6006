# Eliel
# Lecture 5 of 6.006
# Binary Trees

'''
bt is short for binary tree (btree is taken for something else)
'''
class bt (object):
    def __init__(self, key = None, parent = None, \
        left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.key)
    def __int__(self):
        return int(self.key)
    def getKey(self):
        return self.getKey
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getParent(self):
        return self.parent
    def insert(self, key):
        pass
    def find(self, key):
        pass
    def delete(self, key):
        pass
    def display(self, level = 0):
        print (("    " * level) + str(self.key) + ":")
        if self.left != None:
            self.left.display(level + 1)
        if self.right != None:
            self.right.display(level +1)
            
#begin tests

print "hello"
binT = bt(5)
binT.left = bt(3)
binT.right = bt(7)
binT.right.right = bt(20)
binT.right.left = bt(6)
binT.display()