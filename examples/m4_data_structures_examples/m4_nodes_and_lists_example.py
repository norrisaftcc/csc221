
# coding: utf-8

# ## M4 Example
# ###
# ### Data Structures: Linked List

# In Jupyter, manually switch between code and markdown depending on the content of a given cell.
# ### headers use the # symbol in markdown
# ######## more # -> smaller header (such as h1, h2, etc.)
# 
# first let's define a Node class.

# In[1]:


class Node(object):
    def __init__(self, contents=None):
        self.contents = contents
        self.prev = None
        self.next = None
        
    def __repr__(self):
        # string representation (__repr__ and __str__ are equivalent)
        return "Node("+ str(self.contents) +")"
    
    def getPrev(self):
        return self.prev
    
    def setPrev(self, previous=None):
        self.prev = previous
        
    def getNext(self):
        return self.next
    
    def setNext(self, next = None):
        self.next = next


# let's test this class out.

# In[2]:


n1 = Node(1)
n2 = Node('2')
nb = Node('bee')
print(n1)
print(n2)


# We can manually link nodes by setting prev and next.
# 
# (It's best to use getters and setters for this.)

# In[3]:


# create a double-sided link between nodes
n1.setNext(n2)
n2.setPrev(n1)
# due to the default value for the second argument, 
# you can clear next or prev as follows
# (not necessary in this case, just an example)
n2.setNext()

# test
current = n1
print('At', current)
current = current.getNext()
print('At', current)
current = current.getPrev()
print('At', current)


# ### A list class 
# next, we'll create a list class to hold nodes.
# 
# currently, it does little more than keep track of the head node for us.

# In[4]:


class List(object):
    def __init__(self, headNode = None):
        self.head = headNode
        
    def __len__(self):
        length = 0
        current = self.head
        while current != None:
            length += 1
            current = current.getNext()
        return length
    
    def __repr__(self):
        return ("List of size: "+str(len(self)))
        # TODO: traverse the list to print contents
            


# In[5]:


myList = List()
print(myList)
anotherList = List(nb)
print(anotherList)


# Right now everything we do with a list is handled through the Node class instead.
# You might consider what would be involved with implementing the expected features
# to match parity with the default Python list class.
# 
# ### Mapping this to Mazes and Cells
# Right now Nodes have a previous and next reference, which point to other nodes. 
# this allows us to string nodes together in a 'string-of-beads' type linear linked list.
# 
# If instead of prev and next, a Node had a north, south, east, and west, they could be
# linked together in a two dimensional structure. 
# 
# If instead a Node had a parent, left child, and right child, they could be linked together 
# in a binary tree structure. 
# 
# Let's implement those classes.

# In[13]:


# GridNode: can be linked with other nodes in a 2d grid structure
# note: subclassing Node means they also have a prev/next, you may not want this in 
# your implementation. (we'll just ignore them.)

class GridNode(Node):
    def __init__(self, name=None, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        
    def __repr__(self):
        return("GridNode named: "+str(self.name))
    
# we'll leave implementation of getNorth() setNorth() etc. up to you.
# one more thing for convenience: we'll subclass to use a different name.

class Cell(GridNode):
    # init is inherited from GridNode
    
    def __repr__(self):
        return("Cell named: "+str(self.name))
        


# In[16]:


# create four cells
c1 = Cell('Room 1')
c2 = Cell('Room 2')
c3 = Cell('Room 3')
c4 = Cell('Room 4')

# link them as follows: 
# c1 - c2
# |    |
# c3 - c4
#
# c1 <-> c2
c1.east = c2
c2.west = c1

# c1 <-> c3
c1.south = c3
c3.north = c1

# c3 <-> c4
c3.east = c4
c4.west = c3

# c2 <-> c4
c2.south = c4
c4.north = c2



# Let's go on a tour of the cells:

# In[18]:


# simple helper functions to save typing
def imAt(c):
    print("I'm at: ",c)
    
def goTo(c):
    imAt(c)
    return c
    
print('Starting the tour')
loc = c1
imAt(loc)
loc = goTo(loc.east)
loc = goTo(loc.south)
loc = goTo(loc.west)
loc = goTo(loc.north)
print('Tour finished')


# You can add additional code cells, or use the included cell below to continue testing.
# 

# In[20]:


print(loc)

