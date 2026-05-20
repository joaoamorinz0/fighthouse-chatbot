MODALIDADES = {
    "1": "Kickboxing",
    "2": "Boxe",
    "3": "Jiu-Jitsu",
    "4": "Taekwondo"
}

def mensagem_nome():
    return """
📝 MATRÍCULA

Qual é o seu nome?
"""

def mensagem_modalidade():
    return """
🥊 Qual modalidade deseja fazer?

1 - Kickboxing
2 - Boxe
3 - Jiu-Jitsu
4 - Taekwondo
"""

def mensagem_tel():
    return """
Qual é o seu número de telefone?
"""

def validar_modalidade(opcao):
    return MODALIDADES.get(opcao)