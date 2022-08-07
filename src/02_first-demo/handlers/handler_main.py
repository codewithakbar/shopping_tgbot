from handlers.handler_com import HandlerCommands




class HandlerMain:
    """
    Bog'lovchi klass
    """

    def __init__(self, bot):
        
        self.bot = bot
        # ishlov beruvchilarni ishga tushirsh
        self.handler_commands = HandlerCommands(self.bot)

    def handle(self):
        # bu erda ishlov beruvchilar ishlaydi
        self.handler_commands.handle()


    
