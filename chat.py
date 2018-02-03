from chatterbot import ChatBot
import logging

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
        "Edytka",
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.5,
                'default_response': 'W celu wyjaśnienia problemu, prosimy o kontakt z Biurem Obsługi Klienta.'
            }
        ]
    )

info = "Program obecnie jest w fazie uczenia się!\n" \
       "Zdobywa wiedzę z czasem, więc jego odpowiedzi mogą być conajmniej nieodpowiednie.\n" \
       "Prosimy o wyrozumiałość lub kontakt z biurem obsługi klienta.\n" \
       "\nZadaj pytanie, a może Ci odpowiemy.\n"
print(info)

while True:
    try:
        chat = input("Chat > ")	
        if chat != "":
                response = chatbot.get_response(chat)
                print("BOT > " + str(response))

    except(KeyboardInterrupt, EOFError, SystemExit):
        print('\nDziękujemy za skorzystanie z naszego BOTA!\n')
        break

