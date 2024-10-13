class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius>=0:
            ValueError("Radius cannot be negative")
        self._radius=new_radius

    @property
    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def diameter(self):
        return 2 * self._radius