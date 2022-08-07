from telebot.types import KeyboardButton, ReplyKeyboardMarkup
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


    def start_menu(self):
        """
        create buttons on menu
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # Buttnlar joylashuvi
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    
