from sqlalchemy import create_engine, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://user1:user@127.0.0.1:5432/quizential")
DeclarativeBase = declarative_base()    

def db_create_tables(engine):
    """creates the database tables"""
    DeclarativeBase.metadata.create_all(engine)


class Category(DeclarativeBase):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class RSSURL(DeclarativeBase):

    __tablename__ = "rss_urls"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    category = Column(Integer, ForeignKey("categories.id"))


class News(DeclarativeBase):

    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    timestamp = Column(DateTime)
    article_url = Column(String)
    rss_url = Column(Integer, ForeignKey("rss_urls.id"))


if __name__ == "__main__":
    db_create_tables(engine)

