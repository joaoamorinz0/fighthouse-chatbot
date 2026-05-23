from core.chatbot import processar_mensagem

while True:
    try:
        mensagem = input("Cliente: ")
    except EOFError:
        break

    resposta = processar_mensagem("joao", mensagem)

    print(f"\nBot: {resposta}\n")