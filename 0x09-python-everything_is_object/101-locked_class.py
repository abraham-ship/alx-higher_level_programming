#!/usr/bin/python3

"""Creating a locked class"""


class LockedClass:
    """locked class"""
    __slots__ = ['first_name']

    def __setattr__(self, key, value):
        if not hasattr(self, 'first_name') and key != 'first_name':
            raise AttributeError("can't add new attribute")
        super().__setattr__(key, value)
