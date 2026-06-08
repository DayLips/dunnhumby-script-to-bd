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
    # main()
    df = pd.read_csv('data/transaction_data.csv')
    df.info()
    print(df.head())

    # max_len = df['MARITAL_STATUS_CODE'].astype(str).str.len().max()
    # print(f"Максимальная длина: {max_len}")
    # print(df['MARITAL_STATUS_CODE'].unique())