import bot
import logging
import json

if __name__ == '__main__':

    try:
        f = open('./data/botConfig.json')
    except FileNotFoundError:
        print("There was an error opening the file. Please check path in bot.py")
    # f = open('..\\data\\credentials.json')
    config = json.load(f)

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.warning('This will get logged to a file')

    TOKEN = config["botMeta"]["TOKEN"]

    bot.run_discord_bot(TOKEN)
