"""
File: arrays.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
        # logical size starts at zero as the array is empty
        self._logicalsize = 0

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def size(self):
        """-> the logical size (amount actually used) of the array"""
        return self._logicalsize

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        print("getting value",index)
        # check for valid index (>=0 and < logicalsize because it's zero indexed)
        if index < 0:
            raise Exception("index too low, can't set")
        elif index >= self.size():
            raise Exception("index larger than logical size, can't set")
        else:
            return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        print("setting value",index)
        # check for valid index (>=0 and < logicalsize because it's zero indexed)
        if index < 0:
            raise Exception("index too low, can't set")
        elif index >= self.size():
            raise Exception("index larger than logical size, can't set")
        else:
            self._items[index] = newItem





        
