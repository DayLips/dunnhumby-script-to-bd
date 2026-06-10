from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from models import CouponRedempt
from schemas import CouponRedemptCreate

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler('logs/coupon_redempt_repository.log', encoding='utf-8')
    file_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)

class CouponRedemptRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: CouponRedemptCreate) -> Optional[CouponRedempt]:
        try:
            db_redempt = CouponRedempt(**data.model_dump())
            self.db.add(db_redempt)
            self.db.commit()
            self.db.refresh(db_redempt)
            return db_redempt
        except Exception as e:
            logger.error(f"Ошибка при создании записи погашения: {e}")
            self.db.rollback()
            return None
    
    def create_many(self, data_list: List[CouponRedemptCreate]) -> int:
        created_count = 0
        for data in data_list:
            try:
                db_redempt = CouponRedempt(**data.model_dump())
                self.db.add(db_redempt)
                created_count += 1
            except Exception as e:
                logger.error(f"Ошибка при создании: {e}")
                continue
        
        try:
            self.db.commit()
            logger.info(f"Успешно создано {created_count} из {len(data_list)} записей погашений")
        except Exception as e:
            logger.error(f"Ошибка при коммите: {e}")
            self.db.rollback()
            created_count = 0
        
        return created_count
    
    def truncate(self) -> bool:
        try:
            self.db.execute(text("TRUNCATE TABLE raw.coupon_redempt RESTART IDENTITY"))
            self.db.commit()
            logger.info("Таблица coupon_redempt очищена")
            return True
        except Exception as e:
            logger.error(f"Ошибка при очистке таблицы: {e}")
            self.db.rollback()
            return False