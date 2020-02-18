class BaseObj(object):
    def __init__(self, x, y, wx, wy):
        self.x = x
        self.y = y
        self.wy = wy
        self.wx = wx


class ListOfObjects(object):
    def __init__(self):
        self.list = []

    def add(self,item):
        self.list.append(item)

    def clear_list(self):
        self.list.clear()

    def remove_item(self, item):
        self.list.remove(item)

    def traverse(self, **kwargs):
        if 'call_function' in kwargs:
            for item in self.list:
                getattr(
                    item,
                    kwargs['call_function'],
                )(**kwargs)
