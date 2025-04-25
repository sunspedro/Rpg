from colorama import Fore, Style, init
import random
from monstros import criarMonstros
from memorias import memorias
from campoBatalha import planicesDia, planicesNoite, florestaBatalha, florestaFinal

init(autoreset=True)

def reiniciar_jogo(personagem):
    decisao_reinicio = input("\nVocê perdeu... Deseja tentar novamente? (1 para reiniciar, 2 para sair): ")
    if decisao_reinicio == "1":
        print("\nReiniciando o capítulo...\n")
        faseFloresta(personagem)
    elif decisao_reinicio == "2":
        print("\nObrigado por jogar! Até logo!")
        exit()

def florestaIntro(personagem):
    print("\nAo chegar no acampamento você é calorosamente recebido.")
    print(Fore.LIGHTRED_EX + "???:", Fore.RESET, "Quem diria que eles iam ter convencido você HAHAHA.")  # Mitghar
    print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:", Fore.RESET, "Mitghar! É ótimo te ver, pensei que você estivesse na cidade.")
    print(Fore.LIGHTRED_EX + "Mitghar:", Fore.RESET, "Eu estava, mas me pediram para vir pra cá, os goblins estavam mais agitados que o normal.")    
    print(Fore.LIGHTBLUE_EX + "\nMemória atualizada: Mitghar criou você por anos quando seu pai morreu, ele é como um pai pra você.")
    print(Fore.LIGHTRED_EX + "\nMitghar:", Fore.RESET, "Venha, você deve estar com fome da viagem.")
    print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:", Fore.RESET, "Vejo que vocês têm um belo acampamento por aqui, o que estão planejando?")
    print(Fore.LIGHTRED_EX + "Mitghar:", Fore.RESET, "Estamos tentando ganhar território aos poucos, não encontramos nada além de goblins traiçoeiros e armadilhas.")
    print(Fore.LIGHTRED_EX + "Mitghar:", Fore.RESET, "Te desejo sorte garoto, nessa missão não estarei do seu lado o tempo todo.")
    print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:", Fore.RESET, "Os velhos tempos passaram Mitghar, e rápido.")

    print(Fore.LIGHTRED_EX + "\n???", Fore.RESET, "CHEFE, ENCONTRAMOS UM SOBREVIVENTE")
    print("Após esse grito você larga a sopa de javali que estava tomando e corre com Mitghar até a ponta do acampamento.")
    print("Você vê um soldado sem uma perna e 3 enfermeiras em volta.")
    print(Fore.LIGHTRED_EX + "Mitghar:", Fore.RESET, "Misericórdia Eldruel, o que aconteceu com você.")
    print(Fore.LIGHTRED_EX + "Eldruel:", Fore.RESET, "Eu encontrei uma moça, ao chamar ela vi ela correndo para dentro da floresta.")
    print(Fore.LIGHTRED_EX + "Eldruel:", Fore.RESET, "Nisso caí em uma armadilha, um fio mais afiado que qualquer espada que eu já vi.")
    print("Os médicos do acampamento chegam e levam ele para a cabana onde tratam os enfermos.")

    print(Fore.LIGHTRED_EX + "\nMitghar:", Fore.RESET, "É com isso que estamos lidando filho...")
    print("Na sua mente só se passam pensamentos de por que ela fugiu? E o que ela estava fazendo ali?")
    print("Tomado pela sua sede de justiça")
    print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:", Fore.RESET, "Mitghar, vou me preparar e essa noite vou entrar, vou começar aos poucos a vasculhar essa floresta.")
    print("Mitghar apenas sorri para você, ele jamais tentaria te parar depois de anos convivendo com você.")
    print("Você aos poucos se sente mais vivo, a sede de sangue, de completar mais uma missão e de fazer o bem o tomam por inteiro.")
    print("O tempo vai passando e você está pronto para sair.")

def florestaBatalhas(personagem):
    decisao = input("\n1. Prosseguir história\n2. Voltar para a planície\n3. Voltar para a planície noturna\nOpção: ")
    
    if decisao == "1":
        florestaBatalha(personagem)
    elif decisao == "2":
        planicesDia(personagem)
        florestaBatalhas(personagem)
    elif decisao == "3":
        planicesNoite(personagem)
        florestaBatalhas(personagem)

def florestaIntroRei(personagem):
    print("\nApós passar por diversas armadilhas, Goblins e animais, você começa a enxergar o acampamento.")
    print("Várias construções nas árvores de ficar impressionado, muitos animais cantando mas pouco barulho de pessoas ou goblins.")
    print("Você aos poucos se aproxima.")

    print(Fore.LIGHTRED_EX + "\n???", Fore.RESET, "INTRUSOOO!!!")
    print("Você sabe que mesmo que tivessem mil goblins eles não seriam capazes de pará-lo.")
    print("Um goblin vem te atacar e você segura ele pelo pescoço pedindo aonde está o Rei.")
    print(Fore.LIGHTRED_EX + "???", Fore.RESET, "Solte ele de uma vez, ele não tem nada a ver com isso.")

def florestaReiOptions(personagem):
    decisao = input("\n1. Matar o goblin\n2. Soltar\nOpção: ")
    if decisao == "1":
        print("\nVocê aperta o pescoço do goblin e ele morre em sua mão.")
        print("A sede de desespero e a ira percorrem suas veias e te tomam por inteiro.")
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:", Fore.RESET, "AAAAAARGHHTT")
        print("Só um amador pra cair em uma armadilha? Na sede de ódio você esquece do resto do ambiente.")
        print("Um tronco com espinhos bate diretamente nas suas costas, você é arremessado para o pé do Goblin.")
        print(Fore.LIGHTRED_EX + "???:", Fore.RESET, "Eu sou um rei piedoso, mas não vejo um pingo de compaixão no seu coração.")
        print("O Rei coloca o pé na sua cabeça, apesar da pressão você escuta gritos de felicidade dos goblins em volta, o rei explode sua cabeça.")
        print(Fore.LIGHTWHITE_EX + "\nFim.") #dificultar a batalha x boss e colocar ela aqui
        reiniciar_jogo(personagem)           #vitoria = queimar vila ou ir embora e falar a loc | derrota = elartih salva vc e dependendo da memoria ela faz tua cova ou te ajuda
    
    elif decisao == "2":
        print("\nVocê solta o Goblin e ele sai correndo.")
        print(Fore.LIGHTRED_EX + "???", Fore.RESET, "Meu nome é Zarzug, sou o rei, se era isso que você estava procurando.")
        print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "Gostaria de pedir que vá embora, estamos bem resolvidos aqui.")
        print("Você vê pessoas e goblins na janela, mais proximo a você uma criança segurando a mão de um goblin idoso, não consegue entender direito o porquê estão todos juntos.")
        
    escolha = input("1. Estou aqui para libertar todos os que você manteve presos.\n2. Vamos acabar com isso de uma vez por todas.\nO que você decide fazer?")

    if escolha == "1":
        print(Fore.LIGHTRED_EX + "\nZarzug:", Fore.RESET, "Libertar? Hahaha.")
        print("Você escuta todos a sua volta dando risada com o que você acabou de dizer.")
        print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "Todos estão aqui se refugiando bravo guerreiro, nossa comunidade é boa e não queremos guerra com ninguem.")
        print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "A verdadeira tirania é a do rei que você serve.")
        print("Você olha em volta e repara nos olhares de desgosto ao Zarzug citar o rei.")

        escolha2 = input("1.Realmente Zarzug, mas você sabe que tenho uma missão a cumprir.\n2.Não é problema meu o que você acha ou deixa de achar, minha missão sera cumprimida seja Deus ou Diabo me enviando.")
        
    
    elif escolha == "2":
        print("teste")


def faseFloresta(personagem):
    florestaIntro(personagem)
    florestaBatalhas(personagem)
    florestaIntroRei(personagem)
    florestaReiOptions(personagem)
    florestaFinal(personagem)

# print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "")   
