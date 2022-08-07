from telebot.types import KeyboardButton
from settings import config
from data_base.db_alchemy import DBManager

class Keyboards:
    """
    Keyboards klassi bot interfeysini yaratish va belgilash uchun mo'ljallangan
    """

    def __init__(self) -> None:
        self.murkup = None
        self.BD = DBManager()


    def set_btn(self, name, step=0, quantity=0):
        """
        Kirish parametrlari bo'yicha tugmachani yaratadi va qaytaradi
        """
        return KeyboardButton(config.KEYBOARD[name])


