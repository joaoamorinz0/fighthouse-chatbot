from messages.horarios import HORARIOS
from flow.horarios_flow import mostrar_horarios
from messages.modalidades import MODALIDADES
from messages.valores import VALORES
from flow.valores_flow import menu_valores


def mostrar_menu(mensagem):
    
    if mensagem == "1":
        return HORARIOS
    
    elif mensagem == "2":
        return MODALIDADES

    elif mensagem == "3":
        return VALORES

    elif mensagem == "4":
        return """
🔥 AULA EXPERIMENTAL

Lorem ipsum
"""

    elif mensagem == "5":
         return """
Para falar com algum/a antendente, aguarde até entrarmos em contato...
"""

    return """
👊 Bem-vindo à Fight House!

Escolha uma opção:

1 - Horários
2 - Modalidades
3 - Valores
4 - Aula Experimental
5 - falar com atendente
0 - Voltar ao menu
"""