import logging

from database import init_db, SessionLocal
from tools import LoadDunnhumby

def main():
    init_db()
    logger.info("Создание таблиц...")
    db = SessionLocal()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        file_handler = logging.FileHandler('logs/loader.log', encoding='utf-8')
        file_handler.setFormatter(console_formatter)
        logger.addHandler(file_handler)
    try:
        loader = LoadDunnhumby(logger=logger)
        loader.truncate_all_tables(db)
        loader.load_tables(db)
        logger.info("Готово!")
    finally:
        db.close()

if __name__ == '__main__':
    # main()
    logger = logging.getLogger(__name__)
    print(type(logger))