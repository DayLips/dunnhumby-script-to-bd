from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from models import TransactionData
from schemas import TransactionDataCreate

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler('logs/transaction_data_repository.log', encoding='utf-8')
    file_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)

class TransactionDataRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: TransactionDataCreate) -> Optional[TransactionData]:
        try:
            db_trans = TransactionData(**data.model_dump())
            self.db.add(db_trans)
            self.db.commit()
            self.db.refresh(db_trans)
            return db_trans
        except Exception as e:
            logger.error(f"Ошибка при создании транзакции: {e}")
            self.db.rollback()
            return None
    
    def create_many(self, data_list: List[TransactionDataCreate]) -> int:
        created_count = 0
        for data in data_list:
            try:
                db_trans = TransactionData(**data.model_dump())
                self.db.add(db_trans)
                created_count += 1
            except Exception as e:
                logger.error(f"Ошибка при создании транзакции: {e}")
                continue
        
        try:
            self.db.commit()
            logger.info(f"Успешно создано {created_count} из {len(data_list)} транзакций")
        except Exception as e:
            logger.error(f"Ошибка при коммите: {e}")
            self.db.rollback()
            created_count = 0
        
        return created_count
    
    def truncate(self) -> bool:
        try:
            self.db.execute(text("TRUNCATE TABLE raw.transaction_data RESTART IDENTITY"))
            self.db.commit()
            logger.info("Таблица transaction_data очищена")
            return True
        except Exception as e:
            logger.error(f"Ошибка при очистке таблицы: {e}")
            self.db.rollback()
            return False