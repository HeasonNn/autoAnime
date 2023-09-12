from exts import db
from common import *


class AnimeList(db.Model):
    __tablename__ = "anime_list"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    anime_name = db.Column(db.String(40), nullable=True, unique=True)
    mikan_id = db.Column(db.Integer, nullable=False, unique=True)
    img_url = db.Column(db.String(40), nullable=False)
    update_day = db.Column(db.Integer, nullable=False)


class AnimeTask(db.Model):
    __tablename__ = "anime_task"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 任务的默认id
    anime_id = db.Column(db.Integer, nullable=False, unique=True)
    # 剧集对应的番名（AnimeList）的id
    status = db.Column(db.Integer)
    # 下载的状态 0表示还没有开始下载 1表示下载成功 2表示下载开始但是过程失败
    episode = db.Column(db.String(40))
    # 剧集名称


def insert_data_to_anime_list(anime_name, mikan_id, img_url, update_day):
    anime_list = AnimeList(anime_name=anime_name, mikan_id=mikan_id, img_url=img_url, update_day=update_day)
    db.session.add_all([anime_list])
    db.session.commit()


# 初步查询语句 可以修改输入参数
def query_list_by_anime_name():  # 增加过滤条件进行查询
    result = db.session.query(AnimeList).filter(AnimeList.index > 2).all()
    list = []
    for data in result:
        cur = Anime(data.anime_name, data.mikan_id, data.img_url, data.update_day)
        list.append(cur)
        dic = {
            "id": data.index,
            "animeName": data.anime_name,
            "mikan_id": data.mikan_id,
            "img_url": data.img_url,
            "update_day": data.update_day
        }
        print(dic)
        print(cur)

# from sqlalchemy.exc import SQLAlchemyError
# from flask import current_app


# class DbSessionCommit():
#     @staticmethod
#     def add(self):
#         db.session.add(self)
#         return session_commit()

#     @staticmethod
#     def update(self):
#         return session_commit()

#     @staticmethod
#     def delete(self):
#         db.session.delete(self)
#         return session_commit()

# class User(db.Model, DbSessionCommit):
#     __tablename__ = 't_user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)

# def session_commit():
#     try:
#         db.session.commit()
#     except SQLAlchemyError as e:
#         db.session.rollback()
#         reason = str(e)
#         current_app.logger.error(reason)
#         return reason
