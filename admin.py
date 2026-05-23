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


def salvar_leads(leads):
    with open(CAMINHO_LEADS, "w", encoding="utf-8") as arquivo:
        json.dump(
            leads,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def listar_leads():
    leads = carregar_leads()

    if not leads:
        print("\nNenhum lead cadastrado ainda.\n")
        return

    print("\n📋 LISTA DE LEADS\n")

    for lead in leads:
        print(f"ID: {lead.get('id')}")
        print(f"Nome: {lead.get('nome')}")
        print(f"Telefone: {lead.get('telefone')}")
        print(f"Modalidade: {lead.get('modalidade')}")
        print(f"Status: {lead.get('status')}")
        print(f"Criado em: {lead.get('criado_em')}")
        print("-" * 30)


def atualizar_status(novo_status):
    leads = carregar_leads()

    if not leads:
        print("\nNenhum lead cadastrado ainda.\n")
        return

    listar_leads()

    try:
        lead_id = int(input("\nDigite o ID do lead: "))
    except ValueError:
        print("\n❌ ID inválido.\n")
        return

    for lead in leads:
        if lead.get("id") == lead_id:
            lead["status"] = novo_status
            salvar_leads(leads)
            print(f"\n✅ Status atualizado para: {novo_status}\n")
            return

    print("\n❌ Lead não encontrado.\n")


def menu_admin():
    while True:
        print("""
⚙️ PAINEL ADMIN - FIGHT HOUSE

1 - Listar leads
2 - Marcar como contatado
3 - Marcar como matriculado
4 - Marcar como perdido
0 - Sair
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_leads()

        elif opcao == "2":
            atualizar_status("contatado")

        elif opcao == "3":
            atualizar_status("matriculado")

        elif opcao == "4":
            atualizar_status("perdido")

        elif opcao == "0":
            print("\nSaindo do painel...\n")
            break

        else:
            print("\n❌ Opção inválida.\n")


menu_admin()