# jadval tuzilishini tavsiflash uchun kutubxona komponentlari
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# jadvalni ulash modulini import qiling
from sqlalchemy.orm import relationship, backref
# sqlalchemy bilan deklarativ ish uslubi bilan ishlash uchun konstruktor klassi
from sqlalchemy.ext.declarative import declarative_base
# import qilish model modellar to'plami uchun kategoriya
from models.category import Category


# deklarativ uslubni ishga tushirish
Base = declarative_base()


class Products(Base):
    """
    "Mahsulot" jadvalini yaratish uchun sinf,
    sqlalchemy deklarativ uslubiga asoslangan.
    """

    # jadval nomi
    __tablename__ = 'products'

    # jadval maydonlari
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))

    # jadvaldan ma'lumotlarni kaskadli o'chirish uchun
    category = relationship(
        Category,
        backref=backref('products',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f"{self.name} {self.title} {self.price}"


