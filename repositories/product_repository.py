from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from models import Product
from schemas import ProductCreate

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler('logs/products_repository.log', encoding='utf-8')
    file_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: ProductCreate) -> Optional[Product]:
        try:
            db_product = Product(**data.model_dump())
            self.db.add(db_product)
            self.db.commit()
            self.db.refresh(db_product)
            return db_product
        except Exception as e:
            logger.error(f"Ошибка при создании продукта {data.product_id}: {e}")
            self.db.rollback()
            return None
    
    def create_many(self, data_list: List[ProductCreate]) -> int:
        created_count = 0
        for data in data_list:
            try:
                db_product = Product(**data.model_dump())
                self.db.add(db_product)
                created_count += 1
            except Exception as e:
                logger.error(f"Ошибка при создании продукта {data.product_id}: {e}")
                continue
        
        try:
            self.db.commit()
            logger.info(f"Успешно создано {created_count} из {len(data_list)} продуктов")
        except Exception as e:
            logger.error(f"Ошибка при коммите: {e}")
            self.db.rollback()
            created_count = 0
        
        return created_count
    
    def truncate(self) -> bool:
        try:
            self.db.execute("TRUNCATE TABLE raw.products RESTART IDENTITY")
            self.db.commit()
            logger.info("Таблица products очищена")
            return True
        except Exception as e:
            logger.error(f"Ошибка при очистке таблицы: {e}")
            self.db.rollback()
            return False