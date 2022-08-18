from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        """
        Botni foalashtirish
        """
        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def start(self):

        self.handler.handle()
    
    def run_bot(self):
        """Botni ishga tushiradi"""
        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
