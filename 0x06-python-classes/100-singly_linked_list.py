#!/usr/bin/python3
""" define classes for singly linked list"""


class Node:
    """ creates a new Node"""
    def __init__(self, data, next_node=None):
        """ new instance of a Node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieve the data"""
        return (self.__data)

    @data.setter
    def dat(self, value):
        """ set the value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ retrieve the next node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ set value for next_node """
        if (not isinstance(value, Node)) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ define a singly linked list"""
    def __init__(self):
        """ new instance of singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ insert node in correct position """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the printable representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
