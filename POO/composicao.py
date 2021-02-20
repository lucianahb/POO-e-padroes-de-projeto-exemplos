class Funcionario:
 def __init__(self, nome):
  self.__nome = nome
 def retornaNome(self):
  return self.__nome

class Empresa:
 func = []
 def __init__(self):
  print("Empresa Tabajara em funcionamento")
  
  while True:
   print("1. Contratar")
   print("2. Exibir lista de funcionarios")
   op=int( input() )
   
   if op==1:
    self.contratar()
   elif op==2:
    self.exibir()
   else:
    print("Opçao invalida")
 
 def contratar(self):
  nome = input("Nome: ")
  self.func.append( Funcionario(nome) )
 
 def exibir(self):
  for funcionario in self.func:
   print(funcionario.retornaNome())  

Empresa()
