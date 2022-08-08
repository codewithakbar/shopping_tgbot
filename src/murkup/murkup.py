from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
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

    
    def info_menu(self):
        """
        La-la-la
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')

        self.markup.row(itm_btn_1)
        return self.markup


    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup


    @staticmethod
    def remove_menu():
        """
        Menuni ochirish
        """
        return ReplyKeyboardRemove()


    def category_menu(self):
        """
        Mahsulot toifasi menyusidagi tugmalar uchun belgi yaratadi va 
        belgilashni qaytaradi
        """

        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    
