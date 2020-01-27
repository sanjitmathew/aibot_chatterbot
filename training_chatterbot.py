from aibot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

trainer = ChatterBotCorpusTrainer(chatbot)
trainer_list = ListTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

list = []
with open('data_tolokers.txt','r', encoding='utf-8') as file:
    # print(file.read(12)
    for i in file.readlines():
        # print(i)
        list.append(i)

    # print(list)
    trainer_list.train(list)
