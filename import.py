import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine("postgresql://rishigarg:iamafreak123@rishigarg-db-web.ci4m0utla2zy.ap-south-1.rds.amazonaws.com:5432/guitarsongs")
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE requests (id SERIAL PRIMARY KEY, email VARCHAR NOT NULL, song VARCHAR NOT NULL)")
    db.commit()

if __name__ == "__main__":
    main()
