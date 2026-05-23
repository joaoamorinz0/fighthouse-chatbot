import json
import os

from flow.menu import mostrar_menu
from flow.horarios_flow import mostrar_horarios
from flow.valores_flow import menu_valores

from messages.horarios import HORARIOS
from messages.valores import VALORES

from flow.matricula_flow import (
    mensagem_nome,
    validar_modalidade
)


CAMINHO_USUARIOS = "data/usuarios.json"


def carregar_usuarios():
    try:
        with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}


def salvar_usuarios():
    os.makedirs("data", exist_ok=True)

    with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


usuarios = carregar_usuarios()


def criar_usuario_se_nao_existir(usuario_id):
    if usuario_id not in usuarios:
        usuarios[usuario_id] = {
            "estado": "menu",
            "dados": {}
        }

        salvar_usuarios()


def processar_mensagem(usuario_id, mensagem):
    criar_usuario_se_nao_existir(usuario_id)

    mensagem = mensagem.strip().lstrip("\ufeff")

    estado = usuarios[usuario_id]["estado"]
    dados_usuario = usuarios[usuario_id]["dados"]

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
            resposta = "❌ Digite 0 para voltar aos horários."

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
            resposta = "❌ Digite 0 para voltar aos valores."

    elif estado == "matricula_nome":
        dados_usuario["nome"] = mensagem

        estado = "matricula_telefone"

        resposta = """
📱 Qual é o seu número de telefone?

Digite com DDD.
Exemplo: 61999999999
"""

    elif estado == "matricula_telefone":
        dados_usuario["telefone"] = mensagem

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

            resposta = f"""
✅ MATRÍCULA INICIADA

Nome: {dados_usuario["nome"]}
Telefone: {dados_usuario["telefone"]}
Modalidade: {dados_usuario["modalidade"]}

Em breve entraremos em contato!
"""

            estado = "menu"

        else:
            resposta = "❌ Modalidade inválida. Escolha uma opção de 1 a 4."

    else:
        estado = "menu"
        resposta = mostrar_menu("")

    usuarios[usuario_id]["estado"] = estado
    usuarios[usuario_id]["dados"] = dados_usuario

    salvar_usuarios()

    return resposta