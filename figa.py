import os
import errno
from os import path
from collections import UserDict

import yaml


class DotDict(UserDict):
    def __init__(self, dictionary):
        super().__init__()
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self._set(key, DotDict(value))
            else:
                self._set(key, value)

    def _set(self, name, value):
        self.data[name] = value

    def __getattr__(self, name):
        return self.data[name]


class Fig():
    __initialized = False
    __shared_state = {}

    def __init__(self, file, **kwargs):
        self.__dict__ = self.__shared_state
        self._file = file
        self._dir = kwargs.get('dir', os.getcwd())
        if not self._file:
            self._file = kwargs.get('file')
        self._load()
        self.__initialized = True

    def __setattr__(self, key, value):
        if not self.__initialized:
            return super().__setattr__(key, value)
        else:
            return self.set(key, value)

    def __getattr__(self, key):
        if not self.__initialized:
            return super().__getattribute__(key)
        return getattr(self._data, key)

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __repr__(self):
        return repr(self._data)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value

    def _find(self, directory=None):
        if not directory:
            directory = self._dir
        search_path = path.join(directory, self._file)
        if path.isfile(search_path):
            return search_path
        next_path = path.dirname(directory)
        if path.dirname(next_path) == directory:
            return None
        return self._find(next_path)

    def _load(self):
        self._path = self._find()
        if not self._path:
            path = os.path.join(self._dir, self._file)
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
        with open(self._path) as stream:
            d = yaml.safe_load(stream)
            self._data = DotDict(d)
