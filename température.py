class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valeur):
        self.__celsius = valeur

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valeur):
        self.__celsius = (valeur - 32) * 5 / 9


t = Temperature(25)
print("Température en celsius:", t.celsius)
print("Température en fahrenheit:", t.fahrenheit)
t.fahrenheit = 98.6
print("Nouvelle température en celsius:", t.celsius)
