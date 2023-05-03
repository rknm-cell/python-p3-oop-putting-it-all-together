#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = 0, ): 
        self.brand = brand
        self.size = size
       
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")   
    def set_size(self):
        return self._size 
    def get_size(self, value):
        if type(value) == int:
            self._size = value
        else:
            print("size must be an integer")
    size = property(set_size, get_size)
    