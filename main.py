from database import init_db, SessionLocal
import logging

def main():
    init_db()

    db = SessionLocal()

    try:
        ...
    finally:
        db.close()

if __name__ == '__main__':
    # main()
    logger = logging.getLogger(__name__)
    print(type(logger))