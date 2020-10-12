class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    c  = C()
    c.x = "Jeff Cul"
    # NOTE: when you want to get the value, don't add () at the end of the nam
    print(c.x)