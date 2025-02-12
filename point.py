import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_origine(self):
        return math.sqrt(self.__x**2 + self.__y**2)


point1 = Point(3, 4)
print(f"Les coordonnées de ce point sont: {point1.get_x()}, {point1.get_y()}")
print(f"La distance de ce point par rapport à l'origine est: {point1.distance_origine()} ")
