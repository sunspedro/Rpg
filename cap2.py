from colorama import Fore, Style, init
import random
from monstros import criarMonstros
from memorias import memorias
from campoBatalha import planicesDia, planicesNoite, florestaBatalha, florestaFinal, florestaFinalDificil

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
    pass  
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
        print("O rei te chuta para trás e então começa o embate que vai definir que tem a razão")
        
        florestaFinalDificil(personagem)    

        # reiniciar_jogo(personagem) Colocar if pra verificar se venceu          
        # #vitoria = queimar vila ou ir embora e falar a loc | derrota = elartih salva vc e dependendo da memoria ela faz tua cova ou te ajuda
        # se só sair elarith destruiu o acampamento (voce n sabe q foi ela)  criar uma def e reutilizar                                                      
        # se queima a floresta a missão é um fracasso pq a filha do rei ta ali
    elif decisao == "2":
        print("\nVocê afrouxa os dedos e solta o pequeno goblin. Ele não olha para trás apenas corre.")
        print(Fore.LIGHTRED_EX + "???", Fore.RESET, "Zarzug... é como me chamam. Se busca um rei, acho que encontrou um.")
        print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "Não quero confronto. Apenas vá. Já suportamos mais do que deveríamos.")
        print("Do lado de fora, rostos espiam pelas janelas. Crianças humanas e goblins dividem o mesmo espaço, o mesmo medo. Uma pequena mão agarra com força a de um ancião de pele esverdeada.")
        print("Você não entende... ou talvez tema entender demais o que se passa ali.")

        escolha = input("1. Vim libertar aqueles que mantêm presos, mesmo que não saibam disso.\n""2. Já passou da hora. Que essa história termine, de um jeito ou de outro.\n""O que você escolhe?\n")

        if escolha == "1":
            print(Fore.LIGHTRED_EX + "\nZarzug:", Fore.RESET, "Libertar...? Hahaha...")
            print("O som das risadas ao redor não é de deboche, mas de uma dor cansada — como se há muito tempo já tivessem perdido a esperança.")
            print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "Todos aqui estão apenas... tentando sobreviver, bravo guerreiro. Somos uma sombra de um povo que um dia sonhou com a paz.")
            print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "A tirania que conhecemos não vem de monstros... mas de tronos e coroas.")
            print("Você observa os rostos ao redor — não há raiva, apenas uma tristeza silenciosa quando o nome do rei é pronunciado.")

            escolha2 = input("1. Você tem razão, Zarzug... mas meu fardo não muda. A missão continua, mesmo que me afunde junto com ela.\n""2. Pouco me importa o que pensam meu caminho está traçado, mesmo que me leve à ruína.\n")

            if escolha2 == "1":
                print("")   #conversa com zarzug -> ele fala que não roubou nada e conta a verdade sobre a missão / a filha do rei esta ali
                            #o Rei pode te dar algo útil seja item, benção... pode ter uma loja goblin que paga mais caro por coisas "comuns" fora da floresta
                            #voce sempre sera bem vindo / pode voltar
                      
            elif escolha2 == "2":
                pass #batalha normal, mas mesmas opções de queimar floresta/ sair e se só sair elarith destruiu o acampamento (voce n sabe q foi ela)
def faseFloresta(personagem):
    florestaIntro(personagem)
    florestaBatalhas(personagem)
    florestaIntroRei(personagem)
    florestaReiOptions(personagem)
    florestaFinal(personagem)

# print(Fore.LIGHTRED_EX + "Zarzug:", Fore.RESET, "")   
