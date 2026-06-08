from database import init_db, SessionLocal

def main():
    init_db()

    db = SessionLocal()

    try:
        ...
    finally:
        db.close()

if __name__ == '__main__':
    main()