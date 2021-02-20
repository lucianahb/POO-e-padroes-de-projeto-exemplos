class People:
    #ATRIBUTOS DE INSTÂNCIA
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        #atributo privado. Devo utilizar getters e setters
        # para chamá-lo quando necessário
        self.__email = email


class Product:
    #ATRIBUTOS DE CLASSE
    name = 'Apple Pencil'
    description = 'Incredibly easy to use and ready when inspiration strikes.'
    price = 949.90


class Company:
    pass


#ATRIBUTOS DINÂMICOS
c1 = Company()
c1.name = 'Apple'
print(c1.name)
