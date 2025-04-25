from colorama import Fore, Style, init
import random
from monstros import criarMonstros

def planicesDia(personagem):
    monstros = criarMonstros()
    i=0
    j=1
    while i==0:
        optionPlanice = input("\n1.Caçar\n2.Olhar ao redor\n3.Checar mochila\n4.Informações do personagem\n5.Seguir história\nOpção: ")
        if optionPlanice == "1":
            monstroEscolhido = random.choice(monstros["planiceDia"])
            monstroEscolhido.batalha(personagem)
        elif optionPlanice == "2":
            print("\nVocê olha em volta e lembra o quanto andou de cavalo por aqui, percebe que há slimes e cobras ao redor.")
            print("Mas sabe que pode ser mais perigoso durante a noite.")
            print("Se sente solitário por um momento, pensando no caos da cidade que reconforta sua mente vazia.")
            if j==1:
                print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Slimes e cobras são os inimigos da região, você deve tomar cuidado com a noite.")
                j+=1
        elif optionPlanice == "3":
            print("\nVocê checa sua mochila e tem apenas um mapa e algumas frutas para a jornada.")
            print("O mapa mostra que você ainda esta longe do destino, tem um vasto campo para percorrer.")
        elif optionPlanice == "4":
            personagem.exibirInfo()
        elif optionPlanice == "5":
            decisao = input("\nTem certeza? Você não podera voltar antes de prosseguir a história.\n1.Sim\n2.Não\nOpção:")
            if decisao == "1":
                i+=1
            else:
                break

def planicesNoite(personagem):
    monstros = criarMonstros()
    i=0
    j=1
    while i!=10:
            optionPlaniceNoturna = input("\n1.Continuar seu trajeto\n2.Olhar ao redor\n3.Checar mochila\n4.Informações do personagem\nOpção: ")
            if optionPlaniceNoturna == "1":
                monstroEscolhido = random.choice(monstros["planiceNoite"])
                monstroEscolhido.batalha(personagem)
                i+=1
            elif optionPlaniceNoturna == "2":
                print("\nVocê olha em volta e percebe que não vai conseguir passar tão facilmente, talvez terá que lidar com os perigos noturnos.")
                print("Você sente calafrios pelo corpo e percebe que não está sozinho, seja por coisas vivas ou almas vazias.")
                print("Você sabe que a noite é o horário da caça, e você ja lidou com muitos bandidos por essa redondeza.")
                if j==1:
                    print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Bandidos podem rondar esse lugar e você sabe que não vai sair sem encontrar alguns deles.")
                    j+=1
            elif optionPlaniceNoturna == "3":
                print("\nVocê checa sua mochila e percebe que as frutas chegaram ao fim.")
                print("A essa altura seu mapa está todo amassado, por sua sorte você sabe o caminho.")
            elif optionPlaniceNoturna == "4":
                personagem.exibirInfo()

def florestaBatalha(personagem):
    monstros = criarMonstros()
    i=0
    j=0
    while i!=10:
            optionFloresta = input("\n1.Continuar seu trajeto\n2.Olhar ao redor\n3.Checar mochila\n4.Informações do personagem\nOpção: ")
            if optionFloresta == "1":
                monstroEscolhido = random.choice(monstros["floresta"])
                monstroEscolhido.batalha(personagem)
                i+=1
            elif optionFloresta == "2":
                print("\nVocê olha em volta e se sente em casa mesmo após tanto tempo afastado de missões.")
                print("Muitas armadilhas ao seu redor, mas só funcionariam em um amador afoba.")
                print("Varios goblins rondam a área, o pior de tudo são os lanceiros.")
                if j==1:
                    print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Você vai ter que passar por alguns goblins para encontrar o acampamento.")
                    j+=1
            elif optionFloresta == "3":
                print("\nVocê possui uma tocha apagada e materiais para acende-la.")
                print("E também alguns pães que Mitghar te entregou.")
            elif optionFloresta == "4":
                personagem.exibirInfo()

def florestaFinal(personagem):
    monstros = criarMonstros()

    monstroEscolhido = random.choice(monstros["florestaBoss"])
    monstroEscolhido.batalha(personagem)

def florestaFinalDificil(personagem):
    monstros = criarMonstros()

    monstroEscolhido = random.choice(monstros["florestaBossDificil"])
    monstroEscolhido.batalha(personagem)
