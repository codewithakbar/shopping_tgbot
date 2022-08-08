# jadval tuzilishini tavsiflash uchun kutubxona komponentlari
from sqlalchemy import Column, String, Integer, Boolean
# sqlalchemy bilan deklarativ ish uslubi bilan ishlash uchun konstruktor klassi
from sqlalchemy.ext.declarative import declarative_base

# deklarativ uslubni ishga tushirish
Base = declarative_base()


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

    def __str__(self):
        """
        Bu usul sinf ob'ektining satrli tasvirini qaytaradi
        """
        return self.name


