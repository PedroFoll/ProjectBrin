from classes import Classes

class Atributos:

    def gerando_personagem(nome,raca,classe):
        Atributos.status_racas(nome, raca,classe)
        

    def status_racas(nome, raca,classe):

        if raca == 1:
            raca = "Humano"
            For = 10
            Int = 10
            Vit = 10
            Classes.definindo_classe(For, Int, Vit, nome, raca, classe)
            
            

        if raca == 2:
            raca = "Elfo"
            For = 8
            Int = 14
            Vit = 8
            Classes.definindo_classe(For, Int, Vit, nome, raca, classe)
            
        
        if raca == 3 :
            raca = "Orc"
            For = 13
            Int = 6
            Vit = 11
            Classes.definindo_classe(For, Int, Vit, nome, raca, classe)

        if raca == 4:
            raca = "Anão"
            For = 10
            Int = 8
            Vit = 14
            Classes.definindo_classe(For, Int, Vit, nome, raca, classe)