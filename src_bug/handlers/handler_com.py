from .handler import Handler


class HandlerCommands(Handler):
    """
    Guruh kiruvchi /start va /help buyruqlarini va boshqalarni boshqaradi.
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        /start buyrigiga ishlov berish
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' Salom! Keyingi buyrukingizni kutaman.',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # xabarga ishlov berish dekoratori
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)








