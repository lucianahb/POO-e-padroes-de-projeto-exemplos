class Calculadora:

    #Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #método
    def soma(self):
        return self.a + self.b

    #método
    def subtrai(self):
        return self.a - self.b

    #método
    def multiplica(self):
        return self.a * self.b

    #método
    def divide(self):
        return self.a / self.b

c = Calculadora(10, 20)
print(f'Soma: {c.soma()}')