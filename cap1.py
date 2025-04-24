from colorama import Fore, Style, init
import random
from monstros import criarMonstros
from memorias import memorias
from campoBatalha import planicesDia, planicesNoite, florestaBatalha

init(autoreset=True)

def cap1Intro(personagem):
    print("\nMesmo com a sensação de não estar tomando a atitude certa, você se sente livre novamente.")
    print("Lembra dos seus 18 anos no começo do trabalho como guarda, almejando o que conquistou no futuro.")
    print("Andando pela vasta planice você percebe algumas opções.")     

    planicesDia(personagem)

def vilarejo(personagem):
    print("\nVocê continua seguindo seu caminho e chega a um pequeno vilarejo, percebe que a noite está chegando e toma sua desição.")
    decisao = input("1.Passar a noite no vilarejo.\n2.Seguir em busca da floresta.\nOpções: ")

    if decisao == "1":
        print("\nVocê chega a cidade e após achar uma pousada para dormir e vai até a taberna do vilarejo.")
        print("Ao chegar lá você vai até o balcão.")
        print(Fore.LIGHTRED_EX + "Balconista:",Fore.RESET,"O que o estrangeiro vai querer hoje?")
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Ficou tão na cara assim?")
        print(Fore.LIGHTRED_EX + "Balconista:",Fore.RESET,"Todo mundo se conhece aqui em Trevaria, de onde você vem viajante.")
        print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Não deveria esperar diferente mesmo, vim da cidade de Durnvar, mas estou apenas de passagem.")
        print(Fore.LIGHTRED_EX + "Balconista:",Fore.RESET,"Escuto isso todos os dias, meu nome é Vess.")

        decisao2 = input("\nDeseja continuar conversando com Vess?\n1.Sim\n2.Não\nOpção: ")

        if decisao2 == "1":
            print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"É um prazer Vess, pelo visto você é daqui desde sempre.")    
            print(Fore.LIGHTRED_EX + "Vess:",Fore.RESET,"Eu também já viajei por este mundo viajante, minha família é refugiada de Elyvaris.")
            print(Fore.LIGHTRED_EX + "Vess:",Fore.RESET,"Eu era muito nova, não entendo o motivo que fez o reino destruir seu própio território, mas desde então eu vivo aqui.")
            print("Pobre Vess, todos nos passamos por perdas, ela não sabe os motivos e imagino que não gostaria de saber.")
            print(Fore.LIGHTRED_EX + "Vess:",Fore.RESET,"Consigo ver em seus olhos carregam o peso de muitas batalhas.")

            decisao3 = input("\n1.Sim, passei por muita coisa durante minha vida.\n2.Sim, inclusive, lutei na guerra de Elyvaris.\nOpção: ")
            if decisao3 == "1":
                print(Fore.LIGHTRED_EX + "\nVess",Fore.RESET,"De uma olhada no nosso quadro de pedidos, talvez ache algo que te interessa para aproveitar a viagem.")
                print(Fore.LIGHTRED_EX + "Vess",Fore.RESET,"Tenho certeza que é uma grande pessoa, mas minha hora chegou, até mais viajante, faça bom proveito da taberna.")
                print("Você decide aproveitar a deixa e se despedir também, afinal, ainda tem um longo trajeto para percorrer de manhã.")
                print("Você sai da taberna e vê Vess indo embora, como ela já esta a passos distante, você segue seu caminho.")


                print(Fore.LIGHTBLUE_EX + "Memória atualizada: Quadro de pedidos, amanhã vou ver se encontro algo útil.")

            else:
                print(Fore.LIGHTRED_EX + "\nVess:",Fore.RESET,"Você lutou em Elyvaris?")
                print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Sim, foi uma das piores batalhas da minha vida, tinha sangue pra todo lado.")
                print(Fore.LIGHTRED_EX + "Vess:",Fore.RESET,"Os únicos que sobreviveram foram os soldados do rei.")
                print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"E nem todos aliás.")
                print("De repente você sente dois homens te arrastando pra tras pelos braços.")
                print(Fore.LIGHTGREEN_EX + f"{personagem.nome}:",Fore.RESET,"Vocês ficaram malucos me soltem agora!")
                print(Fore.LIGHTRED_EX + "Desconhecidos:",Fore.RESET,"Nunca mais pise nessa taverna, todos nos perdemos nossas famílias graças a suas mãos seu verme.")
                print(Fore.LIGHTRED_EX + "Desconhecidos:",Fore.RESET,"Vá embora e não volte nunca mais para essa cidade sua escória.")
                print("Por ter a lingua maior que a boca você é obrigado a se retirar da taberna, da cidade e seguir caminho.")      
                
                print(Fore.LIGHTBLUE_EX +"\nMemória atualizada:Pelo visto os refugiados de Elyvaris não gostam muito de quem foi responsável pela dizimação do páis deles, essa história não contam nos seus livros...")

                print("Você acaba obrigado a seguir caminho.")
                planicesNoite(personagem)

        elif decisao2 == "2":
            print(Fore.LIGHTGREEN_EX + f"\n{personagem.nome}:",Fore.RESET,"Foi um prazer Vess, mas a noite é curta pra quem sabe onde quer ir.")
            print(Fore.LIGHTRED_EX + "Vess:",Fore.RESET,"Descanse bem viajante, mas saiba que a noite em Trevaria não é tão tranquila quanto parece.")            
            print("Você então sai da taverna, repara nos vagalumes, pessoas na rua, familias e se sente deslocado, como se as traças do remorso te mastigassem por dentro.")
            print("Ao chegar na pousada você descansa.")

            print(Fore.LIGHTBLUE_EX +"\nMemória atualizada: Vilarejo de Trevaria, o nome da Balconista é Vess uma moça simpática, parece acustumada com esse clima, por que a noite não é tranquila?.")

            print("\nPela manhã, a luz pálida de Trevaria entra pela janela, é hora de seguir viagem")

    if decisao == "2":
        planicesNoite(personagem)

def cap1Final(personagem):
    print("\nVocê começa a enxergar o acampamento da resistência à floresta.")
    print("Engraçado pensar que eles querem lutar contra a própia mãe natureza.")
    print(Fore.LIGHTYELLOW_EX +"Fim do primeiro capítulo.")

def fasePlanicies(personagem):  
    cap1Intro(personagem)
    vilarejo(personagem)
    cap1Final(personagem)