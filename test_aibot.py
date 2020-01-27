from aibot import chatbot

while True:
    try:
        user_input = input('user:')

        bot_response = chatbot.get_response(user_input)

        print('Bot:'+bot_response.text)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break