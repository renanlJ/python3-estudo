class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    # Se houver uma chamada "retangulo.area = y" o valor do retorno do método não é alterado.
    # O Python irá criar um novo atributo chamado area com o valor y.
    def obter_area(self):
        return self.__area