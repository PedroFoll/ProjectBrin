
class Personagem:

    def caracteristicas(nome, raca, classe):
        nome = nome
        raca = raca
        classe = classe
        
        if raca == 1:
            print(" Por você ser da raça Humana, seus status basicos serão:\n For = 10 \n Int = 10 \n Vit = 10\n")
        if raca == 2:
            print(" Por você ser da raça Elfo, seus status basicos serão: \n For 8 \n Int = 14 \n Vit = 8\n")
        if raca == 3:
            print(" Por você ser da raça Orc, seus status basicos serão:\n For = 13 \n Int = 6 \n Vit = 11\n")

        #Definindo veriações de classe e raça
        #Humano
        if raca == 1 and classe == 1:
            print ("Você é Humano e Guerreiro, seus status serão \n For = 10 \n Int = 10\n Vit = 15")
        if raca == 1 and classe == 2:
            print("Vocé é Humano e Mago, seus status serão \n For = 10\n Int = 15\n Vit = 10")
        if raca == 1 and classe == 3:
            print("Você é Humano e Assassino, seus status serão \n For = 15\n Int = 10\n Vit = 10")
        #Elfo
        if raca == 2 and classe == 1:
            print ("Você é Elfo e Guerreiro, seus status serão \n For = 8 \n Int = 14\n Vit = 13")
        if raca == 2 and classe == 2:
            print("Vocé é Elfo e Mago, seus status serão \n For = 8\n Int = 19\n Vit = 8")
        if raca == 2 and classe == 3:
            print("Você é Elfo e Assassino, seus status serão \n For = 13\n Int = 14\n Vit = 8")
        #Orc
        if raca == 3 and classe == 1:
            print ("Você é Orc e Guerreiro, seus status serão \n For = 13 \n Int = 6\n Vit = 16")
        if raca == 3 and classe == 2:
            print("Vocé é Orc e Mago, seus status serão \n For = 13\n Int = 11\n Vit = 11")
        if raca == 3 and classe == 3:
            print("Você é Orc e Assassino, seus status serão \n For = 18\n Int = 6\n Vit = 11")