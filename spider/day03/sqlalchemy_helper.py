from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

from mogujie_models import MoguProduct

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/maoyan_db?charset=utf8", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()

def save_db(result_list):
    for item in result_list:
        mogu = MoguProduct()
        mogu.tradeitemid = item['tradeItemId']
        mogu.tradetype = item['tradeType']
        mogu.img = item['img']
        mogu.clienturl = item['clientUrl']
        mogu.link = item['link']
        mogu.itemmarks = item['itemMarks']
        mogu.acm = item['acm']
        mogu.title = item['title']
        mogu.cparam = item['cparam']
        mogu.orgprice = item['orgPrice']
        mogu.hassimilarity = item['hasSimilarity']
        mogu.sale = item['sale']
        mogu.cfav = item['cfav']
        mogu.price = item['price']
        mogu.similarityurl = item['similarityUrl']

        session.add(mogu)
        session.commit()
