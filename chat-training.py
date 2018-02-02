from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import question_and_answers
import logging

logging.basicConfig(level=logging.ERROR)

chatbot = ChatBot("Edytka")

chatbot.set_trainer(ListTrainer)

for conv in question_and_answers.conversation:
    chatbot.train(conv)
