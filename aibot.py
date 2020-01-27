from chatterbot import ChatBot
chatbot = ChatBot('Training Example',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      logic_adapters=[
                          'chatterbot.logic.BestMatch',
                          'chatterbot.logic.MathematicalEvaluation'
                      ],
                      database_uri='sqlite:///database.db'
                  )

