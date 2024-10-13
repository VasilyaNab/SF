class Model:
    def __init__(self):
        self.__name = None
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 3 and len(new_name) <= 15:
            self.__name = new_name