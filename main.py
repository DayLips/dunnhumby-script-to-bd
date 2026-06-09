from database import init_db, SessionLocal
import pandas as pd

def main():
    init_db()

    db = SessionLocal()

    try:
        ...
    finally:
        db.close()

if __name__ == '__main__':
    main()
    # df = pd.read_csv('data/coupon_redempt.csv')
    # df.info()
    # print(df.head())

    # # max_len = df['DESCRIPTION'].astype(str).str.len().max()
    # # print(f"Максимальная длина: {max_len}")
    # # print(df['DESCRIPTION'].unique())