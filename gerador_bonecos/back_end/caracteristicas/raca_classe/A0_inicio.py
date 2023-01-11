from racas import Atributos
from habilidades import Habilidades
from classes import Classes
class Criando_Personagem:

    def recebendo_dados():
        nome = input('Qual seu nome?\n')
        raca = (int(input('Selecione uma raça\n 1 = Humano \n 2 = Elfo \n 3 = Orc\n')))
        classe = (int(input('Qual sua classe? \n 1 = Guerreiro\n 2 = Mago \n 3 = Assassino\n')))

        Atributos.gerando_personagem(nome, raca, classe)
        

