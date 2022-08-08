import abc 

from murkup.murkup import Keyboards
from data_base.db_alchemy import DBManager

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot
        self.keybords = Keyboards()
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass


