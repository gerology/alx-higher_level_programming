0. tests/ : a folder that contains all the test files

1. models/base.py and models/__init__.py : a folder "model" is created where the base.py file and the __nit__.py file that make the folder into a python package are contained

2.models/rectangle.py : Rectangle is a class that inherits from the Base class with attributes of height and width, x and y

3.models/rectangle.py : update the Rectangle class by adding for all setter and getter methods and instantiation with id excluded

4. models/rectangle.py : update Rectangle class by adding public method "def area(self):". it returns the value of rectangle instance

5. models/rectangle.py : update Rectangle class by adding public method "def display(self):". this prints out to stdout the rectangle instance with character #

6. models/rectangle.py : update he rectangle class by overriding the __str__ method so that Rectangle] (<id>) <x>/<y> - <width>/<height> can be returned

7. models/rectangle.py : update Rectangle class by improving the public meyhod"def display(self):" to print in stdout the Rectangle instance with character # taking care of x and y

8. models/rectangle.py : update the rectangle class by adding public method of "def update(self, *args):". it assigns  an argument to each attribute.

9. models/rectangle.py : update Rectangle class by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

10. models/square.py : creates a class Square that inherits from Rectangle class

11. models/square.py : update Square class by adding the public getter and setter size

12. models/square.py : update square class by adding the public method def update(self, *args, **kwargs)

13. models/rectangle.py : Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle

14. models/square.py : Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square

15. models/square.py: Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries

16. models/square.py : Updates the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file

17. models/aquare.py : Updates the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string

18. moels/square.py : Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set

19. models/square.py : Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
