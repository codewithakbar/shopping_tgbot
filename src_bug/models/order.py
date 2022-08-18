# jadval tuzilishini tavsiflash uchun kutubxona komponentlari
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# jadvalni ulash modulini import qiling
from sqlalchemy.orm import relationship, backref
# sqlalchemy bilan deklarativ ish uslubi bilan ishlash uchun konstruktor klassi
from sqlalchemy.ext.declarative import declarative_base
# modellar to'plami uchun mahsulot modelini import qilish
from models.product import Products


# deklarativ uslubni ishga tushirish
from data_base.dbcore import Base

class Order(Base):
    """
    "Buyurtma" jadvalini yaratish uchun sinf,
    sqlalchemy deklarativ uslubiga asoslangan
    """

    # jadval nomi
    __tablename__ = 'orders'

    # jadval maydonlari
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)


    # jadvaldan ma'lumotlarni kaskadli o'chirish uchun
    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        return f"{self.quantity} {self.data}"
