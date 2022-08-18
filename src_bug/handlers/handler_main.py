from handlers.handler_com import HandlerCommands
from handlers.handler_all_text import HandlerAllText
from handlers.handler_inline_query import HandlerInlineQuery


class HandlerMain:
    """
    Bog'lovchi klass
    """

    def __init__(self, bot):

        self.bot = bot
        # ishlov beruvchilarni ishga tushirsh
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        # bu erda ishlov beruvchilar ishlaydi
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()



    
