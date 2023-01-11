
class Classes:

    def definindo_classe(For, Int, Vit, nome, raca, classe):
        if classe == 1 :
                classe = "Guerreiro"
                Vit = Vit+5
        if classe == 2:
                classe = "Mago"
                Int = Int+5
        if classe == 3:
                classe = "Assassino"
                For = For+5

        print(nome+".\nPor você ser da raça "+raca+", e sua Classe ser "+classe+" é seus status basicos serão:\n For = ",For," \n Int = ",Int," \n Vit = ",Vit,"\n")