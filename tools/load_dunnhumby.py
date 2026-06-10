from sqlalchemy.orm import Session
import pandas as pd
import logging

from repositories import (
    CampaignDescRepository, CampaignTableRepository, CouponRedemptRepository,
    CouponRepository, HHDemographicRepository, ProductRepository, TransactionDataRepository
)
from schemas import (
    ProductCreate, CampaignDescCreate, CampaignTableCreate,
    CouponRedemptCreate, CouponCreate, HHDemographicCreate, TransactionDataCreate
)

class LoadDunnhumby:
    SCHEMAS_DICT_LIST = [
        {
            'product_id': 'PRODUCT_ID',
            'manufacturer': 'MANUFACTURER',
            'department': 'DEPARTMENT',
            'brand': 'BRAND',
            'commodity_desc': 'COMMODITY_DESC',
            'sub_commodity_desc': 'SUB_COMMODITY_DESC',
            'curr_size_of_product': 'CURR_SIZE_OF_PRODUCT'
        },
        {
            'description': 'DESCRIPTION',
            'campaign': 'CAMPAIGN',
            'start_day': 'START_DAY',
            'end_day': 'END_DAY'
        },
        {
            'description': 'DESCRIPTION',
            'household_key': 'household_key',
            'campaign_id': 'CAMPAIGN'
        },
        {
            'household_key': 'household_key',
            'day': 'DAY',
            'coupon_upc': 'COUPON_UPC',
            'campaign_id': 'CAMPAIGN'
        },
        {
            'coupon_upc': 'COUPON_UPC',
            'product_id': 'PRODUCT_ID',
            'campaign_id': 'CAMPAIGN'
        },
        {
            'age_desc': 'AGE_DESC',
            'marital_status_code': 'MARITAL_STATUS_CODE',
            'income_desc': 'INCOME_DESC',
            'homeowner_desc': 'HOMEOWNER_DESC',
            'hh_comp_desc': 'HH_COMP_DESC',
            'household_size_desc': 'HOUSEHOLD_SIZE_DESC',
            'kid_category_desc': 'KID_CATEGORY_DESC',
            'household_key': 'household_key'
        },
        {
            'household_key': 'household_key',
            'basket_id': 'BASKET_ID',
            'day':'DAY',
            'product_id': 'PRODUCT_ID',
            'quantity': 'QUANTITY',
            'sales_value': 'SALES_VALUE',
            'store_id': 'STORE_ID',
            'retail_disc': 'RETAIL_DISC',
            'trans_time': 'TRANS_TIME',
            'week_no': 'WEEK_NO',
            'coupon_disc': 'COUPON_DISC',
            'coupon_match_disc': 'COUPON_MATCH_DISC'
        }
        
    ]

    REPOSITORIES_LIST = [
        ProductRepository, CampaignDescRepository, CampaignTableRepository, 
        CouponRedemptRepository, CouponRepository, HHDemographicRepository, TransactionDataRepository
    ]

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def load_tables(self, db, chunk_size: int = 50000):
        table_names = ['product', 'campaign_desc', 'campaign_table', 'coupon_redempt', 'coupon','hh_demographic', 'transaction_data']
        schemas_list = [ProductCreate, CampaignDescCreate, CampaignTableCreate, CouponRedemptCreate, CouponCreate, HHDemographicCreate, TransactionDataCreate]

        self.logger.info("Начинается загрузка таблиц...")
        for i in range(0, len(table_names)):
            self.logger.info(f"Начинаю загрузку {table_names[i]}...")

            try:
                total_loaded = 0
                for chunk in pd.read_csv(f'data/{table_names[i]}.csv', chunksize=chunk_size):
                    validated = []

                    for _, row in chunk.iterrows():
                        try:
                            row_dict = {}
                            schemas_dict = self.SCHEMAS_DICT_LIST[i]
                            for title in schemas_dict:
                                row_dict[title] = row[schemas_dict[title]]
                            
                            validated.append(schemas_list[i](**row_dict))
                        except Exception as e:
                            self.logger.warning(f"Ошибка валидации {table_names[i]}: {e}")
                            continue
                    
                    repo = self.REPOSITORIES_LIST[i](db)
                    count = repo.create_many(validated)
                    total_loaded += count
                    self.logger.info(f"Загружен чанк: {count} {table_names[i]} (всего: {total_loaded})")
            except Exception as e:
                self.logger.error(f"Ошибка загрузки {table_names[i]}: {e}")
    
    def truncate_all_tables(self, db: Session):
        self.logger.warning('!!! ОЧИСТКА ВСЕХ ТАБЛИЦ !!!')

        for reposit in self.REPOSITORIES_LIST:
            repo = reposit(db)
            repo.truncate()

        self.logger.info("Все таблицы очищены")