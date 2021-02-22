class People:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def name(self):
        return f'Name: {self.name}'


class Client(People):
    def __init__(self, name, phone, email, id_client):
        super().__init__(name, phone, email)
        self.id_client = id_client

c1 = Client('Luciana', '11223344', 'luciana@gmail.com', '103')
print(c1.__dict__)