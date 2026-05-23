import json

CAMINHO_LEADS = "data/leads.json"


def carregar_leads():
    try:
        with open(CAMINHO_LEADS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def listar_leads():
    leads = carregar_leads()

    if not leads:
        print("Nenhum lead cadastrado ainda.")
        return

    print("\n📋 LISTA DE LEADS\n")

    for index, lead in enumerate(leads, start=1):
        print(f"{index}. {lead['nome']}")
        print(f"   Telefone: {lead['telefone']}")
        print(f"   Modalidade: {lead['modalidade']}")
        print(f"   Status: {lead['status']}")
        print("-" * 30)


listar_leads()