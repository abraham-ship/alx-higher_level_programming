#!/usr/bin/python3

"""creating square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/setter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assign attributes based on arguments or keyword arguments."""
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square instance."""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
