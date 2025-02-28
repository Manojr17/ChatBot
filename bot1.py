from cleaner import clean_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


CORPUS_FILE="chat.txt"

chatbot= ChatBot("Chatpot")

trainer=ListTrainer(chatbot)
cleaned_corpus = (["what is your name",
                   "i am ai chatbot from ssiet",
                   "is your collage is good at placement",
                   "probably no"])
trainer.train(cleaned_corpus)

exit_conditions = (":q" , "quit", "exit")
while True:
    query = input(">")
    if query in exit_conditions:
        break
    else:
        print(f" {chatbot.get_response(query)} " )