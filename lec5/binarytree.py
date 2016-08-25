# Eliel
# Lecture 5 of 6.006
# Binary Trees

import random

'''
bt is short for binary tree (btree is taken for something else)
'''
class bintree(object):
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
    def setParent(self, tree):
        self.parent = tree
        return self
    def find(self, key):
        if (self.key == key):
            return self
        elif self.left != None and key < self.key:
            return self.left.find(key)
        elif self.right != None and self.key <= key:
            return self.right.find(key)
        else:
            return None 
    def root(self):
        root = self
        while root.parent != None
            root = root.parent
        return root
    def delete(self, dnode):
        if dnode.parent == None: # root node
            #delete parent node
            return dnode
        else:
            if(dnode == parent.left): #left node
                dnode.parent.left = dnode.right
                dnode.parent.insertTree(dnode.left)
                return dnode.parent.root()
            elif(dnode == parent.right): #right node
                dnode.parent.right = dnode.right
                dnode.parent.insertTree(dnode.left)
                return dnode.parent.root()

    def display(self, level = 0):
        print (("        " * level) + str(self.key) + ":")
        if self.left != None:
            self.left.display(level + 1)
        if self.right != None:
            self.right.display(level + 1)
    def insertTree(self, tree):
        if tree.key < self.key:
            if self.left == None: #left
                self.left = tree.setParent(self.left)
                # can do avl balancing if need be
            else:
                # recurively insert into the left sub tree
                self.left.insert(tree)
        if self.key <= tree.key: #right
            if self.right == None:
                self.right = tree.setParent(self.right)
            else:
                self.right.insert(tree)
    def insert(self, key):
        if key < self.key:
            if self.left == None:
                self.left = bintree(key, self)
                # can do avl balancing if need be
            else:
                # recurively insert into the left sub tree
                self.left.insert(key)
        if self.key <= key:
            if self.right == None:
                self.right = bintree(key, self)
            else:
                self.right.insert(key)
        

tree = bintree(int(random.random() * 100))
for x in range(0, 20):
    tree.insert(int(random.random() * 100))
tree.display()

a = tree.find(32)
if a != None:
    print "found 32"
    a.display()
a = tree.find(3)
if a != None:
    print "found 3"
    a.display()
a = tree.find(42)
if a != None:
    print "found 42"
    a.display()
