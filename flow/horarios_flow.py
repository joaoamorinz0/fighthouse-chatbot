from messages.horarios import HORARIOS

def mostrar_horarios(opcao):

    if opcao == "1":
        return """
🥊 HORÁRIOS

KICKBOXING

SEG/QUA/SEX:
08H | INFANTIL: 17H

SEG/QUA:
20H30

SEXTA:
19H00
"""

    elif opcao == "2":
        return """
JIU-JITSU

TER/QUI:
09H
"""

    elif opcao == "3":
        return """
TAEKWONDO

TER/QUI:
17H
"""

    elif opcao == "4":
        return """
BOXE

TER/QUI:
07H

SEG/QUA/SEX:
19H00
"""


    return "Opção inválida."