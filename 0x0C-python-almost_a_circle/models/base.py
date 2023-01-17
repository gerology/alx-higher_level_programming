#!/usr/bin/python3

""" define a base model class """


class Base:
    """ represaentation of a base model

        all other classes inherits from this class

        Atributes:
              __nb_objects (int): number of creared with base class
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize new base

            args:
                id (int): new base identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
