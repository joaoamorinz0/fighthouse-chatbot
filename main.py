from core.chatbot import processar_mensagem

while True:

    mensagem = input("Cliente: ")

    resposta = processar_mensagem(
        "joao",
        mensagem
    )

    print(f"\nBot: {resposta}\n")