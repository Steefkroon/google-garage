# -*- coding: utf-8 -*-
from werkzeug.utils import import_string, cached_property


class LazyView(object):
    def __init__(self, import_name, method_name):
        self.__module__, self.class_name = import_name.rsplit('.', 1)
        self.method_name = method_name
        self.__name__ = self.class_name + '.' + self.method_name + '()'
        self.import_name = import_name

    def __str__(self):
        return self.__name__

    def __repr__(self):
        return "Class: {class_name}, Method: {method_name}".format(
            class_name=self.class_name,
            method_name=self.method_name
        )

    def __call__(self, *args, **kwargs):
        result = self.view().run_before(*args, **kwargs)
        if result:
            return result
        return getattr(self.view(), self.method_name)(*args, **kwargs)

    @cached_property
    def view(self):
        return import_string(self.import_name)
