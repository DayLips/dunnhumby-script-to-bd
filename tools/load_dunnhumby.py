from sqlalchemy.orm import Session
import pandas as pd
import logging

from repositories import (
    CampaignDescRepository, CampaignTableRepository, CouponRedemptRepository,
    CouponRepository, HHDemographicRepository, ProductRepository, TransactionDataRepository
)
from schemas import (
    ProductCreate, CampaignDescCreate, CampaignTableCreate,
    CouponRedemptCreate, CouponCreate
)

class LoadDunnhumby:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    
    def load_products(self, db: Session, csv_path: str = 'data/product.csv', chunk_size: int = 50000):
        self.logger.info("Начинаю загрузку products...")

        try:
            total_loaded = 0

            for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                validated: list[ProductCreate] = []

                for _, row in chunk.iterrows():
                    try:
                        row_dict = {
                            'product_id': row['PRODUCT_ID'],
                            'manufacturer': row['MANUFACTURER'],
                            'department': row['DEPARTMENT'],
                            'brand': row['BRAND'],
                            'commodity_desc': row['COMMODITY_DESC'],
                            'sub_commodity_desc': row['SUB_COMMODITY_DESC'],
                            'curr_size_of_product': row['CURR_SIZE_OF_PRODUCT']
                        }
                        validated.append(ProductCreate(**row_dict))
                    except Exception as e:
                        self.logger.warning(f"Ошибка валидации продукта: {e}")
                        continue
                
                repo = ProductRepository(db)
                count = repo.create_many(validated)
                total_loaded += count
                self.logger.info(f"Загружен чанк: {count} продуктов (всего: {total_loaded})")
            
            self.logger.info(f"Загружено {total_loaded} продуктво")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки products: {e}")

    def load_campaign_desc(self, db: Session, csv_path: str = 'data/campaign_desc.csv', chunk_size: int = 50000):
        self.logger.info("Начинаю загрузку campaign_desc...")

        try:
            total_loaded = 0

            for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                validated: list[CampaignDescCreate] = []

                for _, row in chunk.iterrows():
                    try:
                        row_dict = {
                            'description': row['DESCRIPTION'],
                            'campaign': row['CAMPAIGN'],
                            'start_day': row['START_DAY'],
                            'end_day': row['END_DAY']
                        }
                        validated.append(CampaignDescCreate(**row_dict))
                    except Exception as e:
                        self.logger.warning(f"Ошибка валидации кампании: {e}")
                        continue
                
                repo = CampaignDescRepository(db)
                count = repo.create_many(validated)
                total_loaded += count
                self.logger.info(f"Загружен чанк: {count} кампаний (всего: {total_loaded})")
            
            self.logger.info(f"Загружено {total_loaded} описаний кампаний")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки campaign_desc: {e}")

    def load_campaign_table(self, db: Session, csv_path: str = 'data/campaign_table.csv', chunk_size: int = 50000):
        self.logger.info("Начинаю загрузку campaign_table...")

        try:
            total_loaded = 0

            for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                validated: list[CampaignTableCreate] = []

                for _, row in chunk.iterrows():
                    try:
                        row_dict = {
                            'description': row['DESCRIPTION'],
                            'household_key': row['household_key'],
                            'campaign_id': row['CAMPAIGN']
                        }
                        validated.append(CampaignTableCreate(**row_dict))
                    except Exception as e:
                        self.logger.warning(f"Ошибка валидации: {e}")
                        continue
                
                repo = CampaignTableRepository(db)
                count = repo.create_many(validated)
                total_loaded += count
                self.logger.info(f"Загружен чанк: {count} записей campaign_table (всего: {total_loaded})")
            
            self.logger.info(f"Загружено {total_loaded} записей campaign_table")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки campaign_table: {e}")

    def load_coupon_redempt(self, db: Session, csv_path: str = 'data/coupon_redempt.csv', chunk_size: int = 50000):
        self.logger.info("Начинаю загрузку coupon_redempt...")

        try:
            total_loaded = 0

            for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                validated: list[CouponRedemptCreate] = []

                for _, row in chunk.iterrows():
                    try:
                        row_dict = {
                            'household_key': row['household_key'],
                            'day': row['DAY'],
                            'coupon_upc': row['COUPON_UPC'],
                            'campaign_id': row['CAMPAIGN']
                        }
                        validated.append(CouponRedemptCreate(**row_dict))
                    except Exception as e:
                        self.logger.warning(f"Ошибка валидации: {e}")
                        continue
                
                repo = CouponRedemptRepository(db)
                count = repo.create_many(validated)
                total_loaded += count
                self.logger.info(f"Загружен чанк: {count} записей coupon_redempt (всего: {total_loaded})")
            
            self.logger.info(f"Загружено {total_loaded} записей coupon_redempt")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки coupon_redempt: {e}")

    def load_coupon(self, db: Session, csv_path: str = 'data/coupon.csv', chunk_size: int = 50000):
        self.logger.info("Начинаю загрузку coupon...")

        try:
            total_loaded = 0

            for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                validated: list[CouponCreate] = []

                for _, row in chunk.iterrows():
                    try:
                        row_dict = {
                            'coupon_upc': row['COUPON_UPC'],
                            'product_id': row['PRODUCT_ID'],
                            'campaign_id': row['CAMPAIGN']
                        }
                        validated.append(CouponCreate(**row_dict))
                    except Exception as e:
                        self.logger.warning(f"Ошибка валидации: {e}")
                        continue
                
                repo = CouponRepository(db)
                count = repo.create_many(validated)
                total_loaded += count
                self.logger.info(f"Загружен чанк: {count} записей coupon (всего: {total_loaded})")
            
            self.logger.info(f"Загружено {total_loaded} записей coupon")
        except Exception as e:
            self.logger.error(f"Ошибка загрузки coupon: {e}")