from settings.message import MESSAGES
from settings import config
from handlers.handler import Handler


class HandlerAllText(Handler):
    """
    Klass kiruvchi xabarlarga javob beradi
    """


    def __init__(self, bot):
        super().__init__(bot)
        # maxsulot qatori
        self.step = 0

    def pressed_btn_info(self, message):
        """
        Do'kon haqda info
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.info_menu())

    def pressed_btn_settings(self, message):
        """
        Sozlama tugmasini bosganda....
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.settings_menu())


    def pressed_btn_back(self, message):
        """
        Bir qadam orqa uchun javob beradi
        """
        self.bot.send_message(message.chat.id, "Siz orqaga qaytingiz",
                                reply_markup=self.keybords.start_menu())

    
    def handle(self):

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # * * * * * * * * Menu * * * * * * * * * #

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)
            
