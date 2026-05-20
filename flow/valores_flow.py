from messages.valores import VALORES

def menu_valores(opcao):

    if opcao == "1":
        return """
VALORES INDIVIDUAIS
R$100
"""

    elif opcao == "2":
        return """
PACOTES
2 MODALIDADES - R$: 145,00
3 MODALIDADES - R$: 165,00
4 MODALIDADES - R$: 185,00
"""

    elif opcao == "3":
        return """
PLANO FAMILIAR 
2 PESSOAS - R$: 160,00
3 PESSOAS - R$: 210,00
4 PESSOAS - R$: 230,00
"""




    return "❌ Opção inválida."