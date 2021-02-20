# Programação Orientada a Objetos

## DEFINIÇÃO

*Programação Orientada a Objetos é um paradigma, "é um conjunto de teorias, padrões e métodos que, juntos, representam um modo de organizar o conhecimento"* - HUHN, Thomas. Structure of Scientific Revolution, 1970.

A programação orientada a objetos surgiu com o propósito de ser uma alternativa à programação estruturada, onde as variáveis não são facilmente protegidas caso necessário. Ainda, a POO busca se aproximar ao mundo real, utilizando conceitos como classe, objeto, método.

* <a href="https://www.alura.com.br/artigos/poo-programacao-orientada-a-objetos" target="_blank">Alura - POO</a>

class People:
    def __init__(self, nome, idade, telefone, email):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone
        self.__email = email
    
    def nome(self):
        return f"Nome: {self.__nome}"


class Client(People):
    def __init__(self, nome, idade, telefone, email, id_client):
        super().__init__(nome, idade, telefone, email)
        self.__id_client = id_client

     
c1 = Client('sss', '26', '223311', 'luciana@gmail.com', '444')
print(c1.nome())