from flow.menu import mostrar_menu
from flow.horarios_flow import mostrar_horarios
from flow.valores_flow import menu_valores
from messages.horarios import HORARIOS
from messages.valores import VALORES
from flow.matricula_flow import mensagem_nome, validar_modalidade, mensagem_tel

estado = "menu"
dados_usuario = {}

while True:

    try:
        mensagem = input("Cliente: ").strip().lstrip("\ufeff")
    except EOFError:
        break

    if estado == "menu":

        resposta = mostrar_menu(mensagem)

        if mensagem == "1":
            estado = "horarios"
        
        elif mensagem == "2":
            estado = "modalidades"

        elif mensagem == "3":
            estado = "valores"

        elif mensagem == "4":

            estado = "matricula_nome"

            resposta = mensagem_nome()

    elif estado == "horarios":

        if mensagem == "0":
            estado = "menu"
            resposta = mostrar_menu("")

        else:
            resposta = mostrar_horarios(mensagem)
            if mensagem in ("1", "2", "3", "4"):
                estado = "horarios_detalhe"

    elif estado == "horarios_detalhe":

        if mensagem == "0":
            estado = "horarios"
            resposta = HORARIOS

        else:
            resposta = "Opção inválida. Digite 0 para voltar aos horários."

    elif estado == "valores":

        if mensagem == "0":
            estado = "menu"
            resposta = mostrar_menu("")

        else:
            resposta = menu_valores(mensagem)
            if mensagem in ("1", "2", "3"):
                estado = "valores_detalhe"

    elif estado == "valores_detalhe":

        if mensagem == "0":
            estado = "valores"
            resposta = VALORES

        else:
            resposta = "❌ Opção inválida. Digite 0 para voltar aos valores."

    elif estado == "matricula_nome":

        dados_usuario["nome"] = mensagem

        estado = "matricula_modalidade"

        resposta = """
🥊 Qual modalidade deseja fazer?

1 - Kickboxing
2 - Boxe
3 - Jiu-Jitsu
4 - Taekwondo
"""      

    elif estado == "matricula_modalidade":

        modalidade = validar_modalidade(mensagem)

        if modalidade:
            dados_usuario["modalidade"] = modalidade
            estado = "matricula_tel"
            resposta = mensagem_tel()

        else:
            resposta = "❌ Modalidade inválida. Escolha uma opção de 1 a 4."

    elif estado == "matricula_tel":
        dados_usuario["tel"] = mensagem

        with open("data/leads.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"Nome: {dados_usuario['nome']} | "
                f"Modalidade: {dados_usuario['modalidade']} | "
                f"Telefone: {dados_usuario['tel']}\n"
            )

        resposta = f"""
✅ MATRÍCULA INICIADA

Nome: {dados_usuario['nome']}
Modalidade: {dados_usuario['modalidade']}
Telefone: {dados_usuario['tel']}
"""

        dados_usuario = {}
        estado = "menu"

    print(f"\nBot: {resposta}\n")
