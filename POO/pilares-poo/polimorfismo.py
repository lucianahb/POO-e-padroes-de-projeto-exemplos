class People:
 def register(self):
  print("Olá, sou uma superclasse!")
  
class Client(People):
 def register(self):
  print("Olá, sou uma subclasse!")

class InternClient(Client):
 def register(self):
  print("Olá, sou uma subsubclasse!")

teste = InternClient()
teste.register()