from colorama import Fore, Style, init
import random
from memorias import memorias

init(autoreset=True)


def introZharik(personagem):
    print(f"\nEsse é o começo de sua história meu caro amigo {personagem.nome}.")
    print(f"Você é o melhor {personagem.classe.nome.lower()} da região de Vor...\n") #Vorthen

    print(Fore.LIGHTRED_EX + "???:",Fore.RESET,f"{personagem.nome.upper()}! Que sorte a minha te encontrar aqui, eu e o Mitghar te procuramos pela cidade inteira.\n")

    print(f"Então... esse que acabou de falar é o Zharik, servimos por muito tempo juntos na guarda do rei.")
    print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,"Então siga-me, vamos encontrar o Mitghar que ele veio de longe para te ver.")
    print(Fore.LIGHTBLUE_EX +"\nMemória atualizada: Zharik, seu amigo que serviu com você por anos na guarda do rei.\n")

    print("Chegando no castelo você percebe a presença de antigos conhecidos e de alguns estranhos.")
    print("Na sua mente apenas se passa a vontade de voltar para casa cuidar dos seus animais e da sua familia, você sabe que esta aposentado a muito tempo...\n")

    print(Fore.LIGHTRED_EX + "???:",Fore.RESET,"Hahaha ai está você, sabia que você conseguiria convence-lo Zharik.\n")

    print(Fore.LIGHTBLUE_EX + "A partir de agora as suas desições serão decisivas na história, cada decisão leva para um caminho diferente.")
    print(Fore.LIGHTBLUE_EX + "Os dialogos que você escolher podem fazer as pessoas gostarem ou não de você, e quanto mais elas gostarem...")

def introDurnahael(personagem):
    optionRei = input("1. Zharik é um grande amigo pra mim, jamais deixaria ele na mão hahaha\n2. Eu não me lembro de ter concordado com nada até agora, mas é um prazer\n3. Cumprimentar sem falar nada\nOpção: ") 
    if optionRei == "1":
        print(Fore.LIGHTRED_EX + "???:",Fore.RESET,f"Meu nome é Durnahael, vim direto de Khaldros pois me disseram que na cidade de Durnvar existiam os melhores guerreiros.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,f"Vamos direto ao ponto, caro {personagem.nome}, mas peço que me acompanhe até minha sala.")
        
        print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Durnahael rei de Khaldros, sem muitas informações sobre")

        print("\nNa sala do rei, você percebe joias de ouro, quadros e vê algumas empregadas pelo caminho, que o rei trata com desdem:")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Um artefato antigo foi roubado recentemente.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Você deve procurar pelo rei goblin na floresta, ele roubou um artefato importante para o reino.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Alem do mais ele é perigoso, não podemos deixar ele solto por ai, se é que me entende...")

        print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Sua missão é recuperar o artefato roubado pelo Rei Goblin.")

    elif optionRei == "2":
        print("\nEle franze a sombrancelha ao ouvir sua resposta, claramente irritado.")
        print(Fore.LIGHTRED_EX + "???:",Fore.RESET,f"Corajoso ou tolo... espero que saiba o que está fazendo, {personagem.nome}.")
        print(Fore.LIGHTRED_EX + "???:",Fore.RESET,"Meu nome é Durnahael, vim direto de Khaldros pois me disseram que na cidade de Durnvar existiam os melhores guerreiros.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Zharik me falou sobre você, gostaria de saber se está disposto a realizar coisas grandes.\n")
        memorias = {"respostaErradaDurnahael": True}

        optionReiMissão= input("1.Sempre estive, e Zharik me chamou exatamente por isso pelo que posso imaginar\n2.Tenho muita coisa em jogo nos dias de hoje, não sou mais o mesmo que Zharik conheceu\nOpção: ")

        if optionReiMissão == "1":
            print(Fore.LIGHTRED_EX + "\nDurnahael:",Fore.RESET,f"Muit bem {personagem.nome}, tinha um pé atrás com você, mas pelo visto você é o que as lendas tanto dizem.")
        elif optionReiMissão == "2":
            print(Fore.LIGHTRED_EX + "\nZharik",Fore.RESET,f"Pode não ser mais o mesmo mas ainda é o único, você sabe disso {personagem.nome}, você conhece aquela floresta como ninguem.")
            print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Tudo bem Zharik, sabiamos que não tinha como esperar muito dele.")
            print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"{personagem.nome}, quebra esse galho pelos tempos antigos.")
        print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Bom, então vamos lá, qual a missão?")
        print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"Há muito tempo pessoas tem sumido na floresta {personagem.nome}, nós já não sabemos o que fazer mais.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Alguns soldados da capital se perderam lá e nunca mais voltaram, por isso fui chamado para vir até aqui, e não gostaria de ficar mais muitos dias.")
        print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Então eu só preciso entrar na floresta, descobrir o que está sumindo com as pessoas e resolver o problema? E depois disso estou liberado assim imagino.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,f"Quem sabe {personagem.nome}, quem sabe.")


    else:
        print("\nEle te observa em silêncio intrigado com seu jeito.")
        print(Fore.LIGHTRED_EX + "???:",Fore.RESET,"Reservado, hein? Muito bem, tenho uma tarefa para alguém como você.")
        print(Fore.LIGHTRED_EX + "???:",Fore.RESET,"Meu nome é Durnahael, vim direto de Khaldros pois me disseram que na cidade de Durnvar existiam os melhores guerreiros.")
        print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Bom, então vamos lá, qual a missão?")
        print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"Há muito tempo pessoas tem sumido na floresta {personagem.nome}, nós já não sabemos o que fazer mais.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,"Alguns soldados da capital se perderam lá e nunca mais voltaram, por isso fui chamado para vir até aqui, e não gostaria de ficar mais muitos dias.")
        print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Então eu só preciso entrar na floresta, descobrir o que está sumindo com as pessoas e resolver o problema? E depois disso estou liberado assim imagino.")
        print(Fore.LIGHTRED_EX + "Durnahael:",Fore.RESET,f"Quem sabe {personagem.nome}, quem sabe.")
    
def introElarith(personagem):
    print(Fore.LIGHTRED_EX + "\nZharik:",Fore.RESET,f"Vamos {personagem.nome}, vou te entregar tudo que você precisa para começar.")   
    
    print("\nJá fora do castelo...")
    print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Aonde você me metou Zharik, sabe que eu não faço mais esse tipo de coisas.")
    print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"Sim {personagem.nome}, eu sei, mas entenda que não podemos perder pessoas mais, o reino está desabando com os ataques que vem sofrendo.")
    
    optionIrre = input("\n1.O Rei e o reino que desabem pois não vai ser problema meu, já passou o tempo que eramos guerreiros de um reino decente Zharik.\n2.Você sempre se importou com o povo Zharik, não é atoa que te chamavam de Zharik o irmão de todos.\nOpção: ")

    if optionIrre == "1":
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"O Rei o reino que desabe pois não vai ser problema meu, já passou o tempo que eramos guerreiros de um reino decente Zharik.")
    else:
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Você sempre se importou com o povo Zharik, não é atoa que te chamavam de Zharik o irmão de todos.")
        print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,"Obrigado irmão, você sabe como isso é importante pra mim.")

    print(Fore.LIGHTRED_EX + "???:",Fore.RESET,"Ai está você Zharik.")
    print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"{personagem.nome} essa é Elarith, ela veio de Khaldros tambem, dizem as lendas que é a melhor feiticeira do século.")
    print(Fore.LIGHTRED_EX + "Elarith:",Fore.RESET,f"Obrigado pelos elogios Zharik, é um prazer te conhecer {personagem.nome}, sei tudo o que os livros dizem sobre você.")
    optionIrre = input("\n1.Igualmente Elarith, mas me diga, o que faz a melhor feiticeira de todas por aqui?\n2.Não entendi qual a necessidade de uma feiticeira para uma simples missão...\nOpção: ")
    if optionIrre == "1":
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Igualmente Elarith, mas me diga, o que faz a melhor feiticeira de todas por aqui?")
        print(Fore.LIGHTRED_EX + "Elarith:",Fore.RESET,"Haha, você acha que é o unico que foi designado para uma missão?")
        print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,"Temos mais alguns soldados da capital por aqui, aproveitamos a viagem para resolver todos os problemas existentes.")
    if optionIrre =="2":
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Não entendi qual a necessidade de uma feiticeira para uma simples missão...") 
        print(Fore.LIGHTRED_EX + "Zharik:",Fore.RESET,f"Ninguem disse que ela sera sua companheira {personagem.nome}, ela tem outra missão mais importante.")
        print(Fore.LIGHTRED_EX + "Elarith:",Fore.RESET,"Nos livros tambem dizia que arrogancia era um ponto forte seu...")
        memorias = {"respostaErradaElarith": True}

    print("Zharik te entrega um mapa da floresta que foi resgatado de um cadáver de explorador e diz que você está liberado para a missão.")
    print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Elarith, uma feiticeira forte de Khaldros, mas quão forte ela é? E qual sua missão?\n")
    
def cap0Final(personagem):
    print("Você olha o mapa e sabe que o caminho e conhecido, seus sentidos dizem que é hora de viajar.")
    print(Fore.LIGHTYELLOW_EX +"Fim da introdução.")

def cidadeInicial(personagem):
    introZharik(personagem)
    introDurnahael(personagem)
    introElarith(personagem)
    cap0Final(personagem)






