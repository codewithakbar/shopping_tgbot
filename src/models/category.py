# jadval tuzilishini tavsiflash uchun kutubxona komponentlari
from sqlalchemy import Column, String, Integer, Boolean
# sqlalchemy bilan deklarativ ish uslubi bilan ishlash uchun konstruktor klassi

# deklarativ uslubni ishga tushirish
from data_base.dbcore import Base


class Category(Base):
    """
    Sqlalchemy deklarativ uslubiga asoslangan "mahsulot toifasi" 
    jadvalini tavsiflash uchun sinf modeli.
    """

    # jadval nomi
    __tablename__ = 'category'

    # jadval maydonlari
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __repr__(self):
        """
        Bu usul sinf ob'ektining satrli tasvirini qaytaradi
        """
        return self.name


