#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for k, value in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    value = datetime.strptime(kwargs[k], f)
                if k != '__class__':
                    setattr(self, k, value)

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        clsName = self.__class__.__name__
        nmCls = "[" + clsName + "]"
        dicItem = self.__dict__.items()
        dct = {k: v for (k, v) in dicItem if (not v) is False}
        return nmCls + " (" + self.id + ") " + str(dct)

    def save(self):
        """change the update time to the current
        time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a k and returning
        datemtimes converted to strings
        """
        nWDic = {}
        clsName = self.__class__.__name__
        dicItem = self.__dict__.items()
        frmt = "%Y-%m-%dT%H:%M:%S.%f"
        for k, v in dicItem:
            if k == "created_at" or k == "updated_at":
                nWDic[k] = v.strftime(frmt)
            else:
                if not v:
                    pass
                else:
                    nWDic[k] = v
        nWDic['__class__'] = clsName

        return nWDic

