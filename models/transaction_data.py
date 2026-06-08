from sqlalchemy import Column, Integer, BigInteger, Float

from database import Base

class TransactionData(Base):
    __tablename__ = 'transaction_data'
    __table_args__ = {'schema': 'raw'}

    household_key = Column(BigInteger, nullable=False, index=True) # Индекс для поиска по домохозяйствам
    basket_id = Column(BigInteger, nullable=False, index=True)     # Индекс для группировки по корзинам
    day = Column(Integer, nullable=False, index=True)              # Индекс для фильтрации по датам
    product_id = Column(Integer, nullable=False, index=True)       # Индекс для связывания с товарами
    quantity = Column(Integer, nullable=False)
    sales_value = Column(Float, nullable=False)
    store_id = Column(Integer, nullable=False, index=True)         # Индекс для анализа по магазинам
    retail_disc = Column(Float, nullable=True)
    trans_time = Column(Integer, nullable=True)
    week_no = Column(Integer, nullable=False, index=True)          # Индекс для временного анализа
    coupon_disc = Column(Float, nullable=True)
    coupon_match_disc = Column(Float, nullable=True)

    def __repr__(self):
        return f"<TransactionData(basket_id={self.basket_id}, product_id={self.product_id})>"