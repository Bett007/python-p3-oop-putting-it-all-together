# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        # use the property setter so validation applies on init too
        self.size = size
        # default condition
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        """
        'Repairs' the shoe:
        - sets condition to 'New'
        - prints a message about being repaired
        """
        self.condition = "New"
        print("Your shoe is as good as new!")

