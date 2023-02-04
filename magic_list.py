from collections import UserList
from dataclasses import dataclass


class MagicList(UserList):
    def __init__(self, class_type=None):
        super().__init__()
        self.class_type = class_type

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            if self.class_type:
                self.data.append(self.class_type())
                return self.data[index]

    def __setitem__(self, index, value):
        try:
            self.data[index] = value
        except IndexError:
            if index > len(self.data):
                raise
            else:
                if self.class_type:
                    self.data.append(self.class_type(value))
                else:
                    self.data.append(value)
