class People:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.__email = email

#criação do objeto p1
p1 = People('Luciana', '1122334455', 'luciana.barbosa@olist.com')
print(p1.name)
#print(p1.self.__email) #não vai ser lido porque é privado

#criação do objeto p2
p2 = People('teste', '1122', 'teste.teste@olist.com')
print(p2.name, p2.phone)