#!/usr/bin/python3
#<doha> and <youssef>
""" Class BaseModel """
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """defines attributes id,
    created_at, updated_at and methods
    """

    def __init__(self, *args, **kwargs):
        """constructor for class attrs id
        created_at and updated_at
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                      def __str__(self):
        """ the String """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ save the function """
        self.updated_at = datetime.now()
        models.storage.save()
        def to_dict(self):
        """returns a dictionary repr of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict

