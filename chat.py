from chatterbot import ChatBot
import logging

logging.basicConfig(level=logging.ERROR)

chatbot = ChatBot(
        "Edytka",
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.35,
                'default_response': 'Nie rozumiem. Może powtórzyć pytanie?'
            }
        ],
        # read_only=True,
    )

while True:
    try:
        chat = input("Chat > ")
        response = chatbot.get_response(chat)
        print("BOT > " + str(response))
    except(KeyboardInterrupt, EOFError, SystemExit):
        print('\nDziękujemy za skorzystanie z naszego BOTA!\n')
        break
